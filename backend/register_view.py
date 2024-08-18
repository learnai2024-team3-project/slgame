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
from backend.models import Player, UserTab
from backend.serializers import PlayerSerializer
from backend.serializers import AuthLoginRequestSerializer,\
      UploadRequestSerializer,\
      StartGameRequestSerializer, SubmitGameRequestSerializer, RegisterRequestSerializer


@swagger_auto_schema(
        methods=['POST'],
        request_body = RegisterRequestSerializer,
        responses = { 
            status.HTTP_200_OK: openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties = {
                'client_id': openapi.Schema(type=openapi.TYPE_STRING),
                'mail': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING)

            }
    )},
)


@api_view(['POST'])
def register(request):

    serializer = RegisterRequestSerializer(data=request.data) 

    if serializer.is_valid() == False:
            return JsonResponse({
                "status": "fail to deserialize",
                "feedback": "",
                "data":{
                    "client_id": "",
                    "mail": "",
                    "password":"" 
                }
                }, safe=False)
    
        # 取username和score
    userid = serializer.validated_data["client_id"]
    useremail = serializer.validated_data["mail"]
    password = serializer.validated_data["password"]
    
    # user = UserTab.objects.filter(userid=userid).first()

    try:
        if UserTab.objects.get(userid=userid):
            print(f'重複建立使用者帳號{userid}')
            return JsonResponse({
                "error": f"重複建立使用者帳號{userid}",
            }, safe=False)
        
    except UserTab.DoesNotExist:
         UserTab.objects.create(userid=userid, useremail=useremail, password=password)
         return JsonResponse({
              'message': '成功建立使用者帳號'
         }, safe=False)