from django.shortcuts import render
from django.http import JsonResponse
from django.db import transaction
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from backend.models import Player 
from backend.serializers import PlayerSerializer
from backend.serializers import AuthLoginRequestSerializer,\
      UploadRequestSerializer,\
      StartGameRequestSerializer, SubmitGameRequestSerializer

@swagger_auto_schema(
    methods=['POST'],
    request_body = StartGameRequestSerializer,
    responses = { 
            status.HTTP_200_OK: openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties = {
                'status': openapi.Schema(type=openapi.TYPE_STRING),
                'gameId': openapi.Schema(type=openapi.TYPE_STRING),
                "challenge": {
                    "type": openapi.Schema(type=openapi.TYPE_STRING),
                    "content": openapi.Schema(type=openapi.TYPE_STRING)
                },
            }
    )},
)
@api_view(['POST'])
def game_start(request):
    return JsonResponse({
        "status": "success",
        "gameId": "1",
        "challenge": {
            "type": "A",
            "content": "Apple"
        }
    }, safe=False)