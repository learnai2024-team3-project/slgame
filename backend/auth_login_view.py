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

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount

# Create your views here.
from backend.models import Player 
from backend.serializers import PlayerSerializer
from backend.serializers import AuthLoginRequestSerializer,\
      UploadRequestSerializer,\
      StartGameRequestSerializer, SubmitGameRequestSerializer

@swagger_auto_schema(
        methods=['POST'],
        request_body = AuthLoginRequestSerializer,
        responses = { 
            status.HTTP_200_OK: openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties = {
                'token': openapi.Schema(type=openapi.TYPE_STRING),
                'expiresIn': openapi.Schema(type=openapi.TYPE_INTEGER)
            }
    )},
)
@api_view(['POST'])
def auth_login(request):
    return JsonResponse({
        "token": "123456",
        "expiresIn": 65535
    }, safe=False)

# Create your views here.
@login_required(login_url='log-in')
def main(request):
    """首頁(個人資訊)
    """
    social_auth_user = SocialAccount.objects.get(user=request.user)
    provider = social_auth_user.provider
    items = social_auth_user.extra_data.items()

    return render(request, 'main.html', locals())


def log_in(request):
    """登入頁面
    """
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')


def log_out(request):
    """登出
    """
    logout(request)
    return redirect('/')