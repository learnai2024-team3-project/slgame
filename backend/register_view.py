import uuid
from django.shortcuts import render
from django.http import JsonResponse
from django.db import transaction
from django.urls import reverse
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
                "status": "fail",
                "errortype": "repeatuserid",
                "error": f"重複建立使用者帳號{userid}",
            }, safe=False)
        
    except UserTab.DoesNotExist:
         UserTab.objects.create(userid=userid, useremail=useremail, password=password)
         user = UserTab.objects.get(userid=userid);
         user.login_token = uuid.uuid4().hex  # 生成新的 token
         user.save(update_fields=['login_token', 'last_login_time'])  # 更新 token 和最後登入時間
    
         return JsonResponse({
              "status": "success",
              'message': '成功建立使用者帳號',
              "userid": userid,  
              "loginToken": user.login_token,
         }, safe=False)