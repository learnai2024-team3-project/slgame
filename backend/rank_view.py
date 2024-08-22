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

# @swagger_auto_schema(
#     methods=['GET'],
#     query_serializer=RankQuerySerializer,
#     responses={
#         status.HTTP_200_OK: openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'count': openapi.Schema(type=openapi.TYPE_INTEGER),
#                 'rank': openapi.Schema(type=openapi.TYPE_INTEGER),
#                 'users': openapi.Schema(
#                     type=openapi.TYPE_ARRAY,
#                     items=openapi.Schema(
#                         type=openapi.TYPE_OBJECT,
#                         properties={
#                             'userid': openapi.Schema(type=openapi.TYPE_STRING),
#                             'score': openapi.Schema(type=openapi.TYPE_INTEGER),
#                         }
#                     )
#                 )
#             }
#         )
#     }
# )

@api_view(['GET'])
def get_rank(request):
    # serializer = RankQuerySerializer(data=request.GET)
    
    # if serializer.is_valid() == False:
    #     return JsonResponse({
    #         "status": "fail to deserialize",
    #         "feedback": "",
    #     }, safe=False)

    # userid = serializer.validated_data["client_id"]

    userid = request.GET.get('userid') 

    try:
        user = UserTab.objects.get(userid=userid)
        if user:
            # 獲取用戶排名
            users = UserTab.objects.order_by('-totalscore')
            rank = list(users).index(user) + 1
            score = user.totalscore

            # 總使用者人數
            total_users = users.count()

            # 取前三名的玩家與成績
            top_three_users = users[:3]
            top_three = [{'userid': u.userid, 'score': u.totalscore, 'rank': idx + 1} for idx, u in enumerate(top_three_users)]

            return JsonResponse({
                "status": "success",
                "rank": rank,
                "score": score,
                "count": total_users,
                "users": top_three,
            }, safe=False)
        else:
            return JsonResponse({
                "status": "fail",
                "message": f"無此{userid}使用者",
            }, safe=False)

    except UserTab.DoesNotExist:
        return JsonResponse({
            "status": "fail",
            "message": f"無此{userid}使用者",
        }, safe=False)
