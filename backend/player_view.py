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

# Create your views here.
from backend.models import Player 
from backend.serializers import PlayerSerializer
from backend.serializers import AuthLoginRequestSerializer,\
      UploadRequestSerializer,\
      StartGameRequestSerializer, SubmitGameRequestSerializer

class PlayerView(GenericAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    # Get 請求 回傳所有玩家
    def get(self, request, *args, **kargs):
        players = self.get_queryset()
        serializer = self.serializer_class(players, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)