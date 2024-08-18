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
import os
from rest_framework.parsers import JSONParser
from PIL import Image
from io import BytesIO
from django.views.decorators.gzip import gzip_page
from backend.recognize_view import recognize_image
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

        with Image.open(BytesIO(image_byte)) as img:
            pil_image = img.convert('RGB')
            open_cv_image = numpy.array(pil_image)
            open_cv_image = open_cv_image[:, :, ::-1].copy()
            (recognizedWord, confidence) = recognize_image(open_cv_image)
            print(recognizedWord)

        return JsonResponse({
            "status": "success",
            "feedback": "",
            "data": {
                "recognizedWord": recognizedWord,
                "confidence": str(confidence)
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
