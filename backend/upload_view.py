from django.shortcuts import render
from django.http import JsonResponse
from django.db import transaction
from rest_framework.generics import GenericAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
import base64
import cv2
from rest_framework.parsers import JSONParser
from PIL import Image
from io import BytesIO
from django.views.decorators.gzip import gzip_page
from backend.recognizer import recognize_image, recognize_video
import numpy


# Create your views here.
from backend.models import Player 
from backend.serializers import PlayerSerializer
from backend.serializers import AuthLoginRequestSerializer,\
      UploadRequestSerializer,\
      StartGameRequestSerializer, SubmitGameRequestSerializer

@swagger_auto_schema(
        methods=['POST'],
        request_body = UploadRequestSerializer,
        responses = { 
            status.HTTP_200_OK: openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties = {
                'status': openapi.Schema(type=openapi.TYPE_STRING),
                'feedback': openapi.Schema(type=openapi.TYPE_INTEGER),
                "schema": {
                    "recognizedWord": openapi.Schema(type=openapi.TYPE_STRING),
                    "confidence": openapi.Schema(type=openapi.FORMAT_FLOAT)
                },
            }
    )},
)
@api_view(['POST'])
@gzip_page
def upload_video(request):
    try:
        pythondata = JSONParser().parse(request)
        serializer = UploadRequestSerializer(data=pythondata) 

        if serializer.is_valid() == False:
            return JsonResponse({
                "status": "fail to deserialize",
                "feedback": "",
                "data": {
                    "recognizedWord": "",
                    "confidence": ""
                }
                }, safe=False)
    
        file_byte = base64.b64decode(serializer.validated_data["file"])
        (recognizedWord, confidence) = recognize_video(file_byte)
        #recognizedWord = "A"
        #confidence = 99.9

        return JsonResponse({
            "status": "success",
            "feedback": "",
            "data": {
                "recognizedWord": recognizedWord,
                "confidence": str(confidence)
            }
        }, safe=False)
        
    except BaseException as e:
        print(str(e))
        return JsonResponse({
                "status": str(e),
                "feedback": "",
                "data": {
                    "recognizedWord": "",
                    "confidence": ""
                }
                }, safe=False)

@swagger_auto_schema(
        methods=['POST'],
        request_body = UploadRequestSerializer,
        responses = { 
            status.HTTP_200_OK: openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties = {
                'status': openapi.Schema(type=openapi.TYPE_STRING),
                'feedback': openapi.Schema(type=openapi.TYPE_INTEGER),
                "schema": {
                    "recognizedWord": openapi.Schema(type=openapi.TYPE_STRING),
                    "confidence": openapi.Schema(type=openapi.FORMAT_FLOAT),
                    "recognizedImage": openapi.Schema(type=openapi.TYPE_STRING)
                },
            }
    )},
)
@api_view(['POST'])
@gzip_page
def upload(request):
    try:
        pythondata = JSONParser().parse(request)
        serializer = UploadRequestSerializer(data=pythondata)

        if not serializer.is_valid():
            return JsonResponse({
                "status": "fail to deserialize",
                "feedback": "",
                "data": {
                    "recognizedWord": "",
                    "confidence": ""
                }
                }, safe=False)

        image_byte = base64.b64decode(serializer.validated_data["file"])

        recognizedWord = ""
        recognizedImage = ""

        with Image.open(BytesIO(image_byte)) as img:
            pil_image = img.convert('RGB')
            open_cv_image = numpy.array(pil_image)
            open_cv_image = open_cv_image[:, :, ::-1].copy()
            open_cv_image = cv2.flip(open_cv_image, 1)
            (recognizedWord, confidence) = recognize_image(open_cv_image)
            _, buffer = cv2.imencode('.png', open_cv_image)
            recognizedImage = base64.b64encode(buffer).decode('utf-8')
            print(recognizedWord)
        
        return JsonResponse({
            "status": "success",
            "feedback": "",
            "data": {
                "recognizedWord": recognizedWord,
                "confidence": str(confidence),
                "recognizedImage": recognizedImage
            }
        }, safe=False)

    except BaseException as e:
        return JsonResponse({
                "status": str(e),
                "feedback": "",
                "data": {
                    "recognizedWord": "",
                    "confidence": ""
                }
                }, safe=False)
