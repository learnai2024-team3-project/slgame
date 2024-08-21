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

from backend.models import Player 
from backend.serializers import PlayerSerializer
from backend.serializers import AuthLoginRequestSerializer,\
      UploadRequestSerializer,\
      StartGameRequestSerializer, SubmitGameRequestSerializer


# Create your views here.
def index(request):
    project_name = "Sign Language Game Project"
    return render(request, "index.html", locals())


# def wordle_view(request, userid=None):
#     title = "Wordle AI - Sign Language Edition"
#     return render(request, 'wordle2.html', locals())

def wordle_view(request):
    userid = request.GET.get('userid')
    title = "Wordle AI - Sign Language Edition"
    context = {'userid': userid}
    return render(request, 'wordle3.html', context)


def tutorial_view(request):
    return render(request, 'tutorial.html')


def auth_login_view(request):
    return render(request, 'login.html')


def register_view(request):
    return render(request, 'register.html')
