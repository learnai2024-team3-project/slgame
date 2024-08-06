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
    request_body = SubmitGameRequestSerializer,
    responses = { 
            status.HTTP_200_OK: openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties = {
                'status': openapi.Schema(type=openapi.TYPE_STRING),
                'store': openapi.Schema(type=openapi.TYPE_INTEGER),
                'correct': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                "ranking": {
                    "position": openapi.Schema(type=openapi.TYPE_INTEGER),
                    "totalPlayers": openapi.Schema(type=openapi.TYPE_INTEGER)
                },
            }
    )},
)
@api_view(['POST'])
def submit_game(request):
    return JsonResponse({
        "status": "success",
        "store": 100,
        "correct": True,
        "ranking": {
            "position": 5,
            "totalPlayers": 1
        }
    }, safe=False)