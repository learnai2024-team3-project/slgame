
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
    return render(request, 'wordle3.html', locals())


def tutorial_view(request):
    return render(request, 'tutorial.html')


def auth_login_view(request):
    return render(request, 'login.html')
