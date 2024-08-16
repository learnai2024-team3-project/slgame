
import base64
import cv2
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
from django.db import transaction
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.middleware.gzip import GZipMiddleware
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from backend.recognizer import recognize_image
from backend.models import Player 
from backend.serializers import PlayerSerializer
from backend.serializers import AuthLoginRequestSerializer,\
      UploadRequestSerializer,\
      StartGameRequestSerializer, SubmitGameRequestSerializer


# Create your views here.
def index(request):
    project_name = "Sign Language Game Project"
    return render(request, "index.html", locals())


def wordle_view(request):
    title = "Wordle AI - Sign Language Edition"
    return render(request, 'wordle.html', locals())


def tutorial_view(request):
    return render(request, 'tutorial.view')


@csrf_exempt
def recognize_view(request):
    if request.method == 'POST':
        data = request.json()  # Parse JSON data from the request
        image_data = data.get('image')  # Get the image data

        # Decode base64 image data to an image format
        _, image_encoded = image_data.split(',', 1)
        image_bytes = base64.b64decode(image_encoded)
        image_array = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        # Perform recognition using the YOLO model
        label, confidence = recognize_image(image)

        # Return the recognition result as JSON
        return JsonResponse({'label': label, 'confidence': confidence})

    # Return an error response if the request method is not POST
    return JsonResponse({'error': 'Invalid request method.'}, status=400)
