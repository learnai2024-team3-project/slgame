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
from django.middleware.gzip import GZipMiddleware


# Create your views here.
from backend.models import Player 
from backend.serializers import PlayerSerializer
from backend.serializers import AuthLoginRequestSerializer,\
      UploadRequestSerializer,\
      StartGameRequestSerializer, SubmitGameRequestSerializer


def index(request):
    project_name = "Sign Language Game Project"
    return render(request, "index.html", locals())


def wordle(request):
    title = "Wordle AI - Sign Language Edition"
    return render(request, 'wordle.html', locals())
