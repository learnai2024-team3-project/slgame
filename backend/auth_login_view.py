import uuid
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
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from backend.models import Player, UserTab
from backend.serializers import PlayerSerializer
from backend.serializers import AuthLoginRequestSerializer,\
      UploadRequestSerializer,\
      StartGameRequestSerializer, SubmitGameRequestSerializer

from django.urls import reverse
from django.utils import timezone

@swagger_auto_schema(
        methods=['POST'],
        request_body = AuthLoginRequestSerializer,
        responses = { 
            status.HTTP_200_OK: openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties = {
                'client_id': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING)
            }
    )},
)


@api_view(['POST'])
def other_login(request):

    serializer = AuthLoginRequestSerializer(data=request.data) 

    if serializer.is_valid() == False:
            return JsonResponse({
                "status": "fail to deserialize",
                "feedback": "",
                "data":{
                    "client_id": "",
                    "password":""
                }
                }, safe=False)
    
        # 取username和score
    userid = serializer.validated_data["client_id"]
    password = serializer.validated_data["password"]
    
    try:
        user = UserTab.objects.get(userid=userid)
        if user:
              if user.password == password:
                  
                    user.last_login_time = timezone.now();
                    # print(user.last_login_time);
                    # user.save();

                    user.login_token = uuid.uuid4().hex  # 生成新的 token
                    user.save(update_fields=['login_token', 'last_login_time'])  # 更新 token 和最後登入時間

                    print(f'登入成功')
                    # target_url = reverse('wordle', kwargs={'userid': userid})
                    # print(target_url)
                    return JsonResponse({
                        "status": "success",
                        "message": "Login successful", 
                        # "redirect_url": target_url,  
                        'userid': userid, 
                        "loginToken": user.login_token,
                    }, safe=False)
              else:
                    print(f'密碼輸入錯誤')
                    return JsonResponse({
                        "status": "fail",
                        "message": "Invalid password",
                    }, safe=False) 

    except:
          print(f'無此{userid}使用者')
          return JsonResponse({
                "status": "fail",
                "message": f"無此{userid}使用者",
          }, safe=False)
