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
def upload(request):
    return JsonResponse({
        "status": "success",
        "feedback": "",
        "data": {
            "recognizedWord": "A",
            "confidence": "float"
        }
    }, safe=False)

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

class PlayerView(GenericAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    # Get 請求 回傳所有玩家
    def get(self, request, *args, **kargs):
        players = self.get_queryset()
        serializer = self.serializer_class(players, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)

def index(request):
    project_name = "Sign Language Game Project"
    return render(request, "index.html", locals())