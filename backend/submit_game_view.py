import traceback
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
from rest_framework.parsers import JSONParser

# Create your views here.
from backend.models import Player 
from backend.serializers import PlayerSerializer
from backend.serializers import AuthLoginRequestSerializer,\
      UploadRequestSerializer,\
      StartGameRequestSerializer, SubmitGameRequestSerializer
from backend.models import UserTab 
# from django.db import transaction

@swagger_auto_schema(
    methods=['POST'],
    request_body = SubmitGameRequestSerializer,
    responses = { 
            status.HTTP_200_OK: openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties = {
                'status': openapi.Schema(type=openapi.TYPE_STRING),
                'feedback': openapi.Schema(type=openapi.TYPE_INTEGER),
                'data': {
                    'totalscore': openapi.Schema(type=openapi.TYPE_INTEGER),
                    "count":openapi.Schema(type=openapi.TYPE_INTEGER),
                    "rank":openapi.Schema(type=openapi.TYPE_INTEGER),
                    }
                
            
                # 'data': openapi.Schema(
                #     type=openapi.TYPE_OBJECT,
                #     properties={
                #         'totalscore': openapi.Schema(type=openapi.TYPE_INTEGER),
                #     }
                #     ),
               
                
            }
    )},
)

@api_view(['POST'])
def submit_game(request):

    try:

        # pythondata = JSONParser().parse(request)
        serializer = SubmitGameRequestSerializer(data=request.data) 

        if serializer.is_valid() == False:
            return JsonResponse({
                "status": "fail to deserialize",
                "feedback": "",
                "data":{
                    "totalscore": "",
                    "count": "",
                    "rank": "",
                
                }
                }, safe=False)
    
        # 取username和score
        userid = serializer.validated_data["userid"]
        score = serializer.validated_data["score"]
        token = serializer.validated_data["token"]

        # print(username)
        # print(score)

        user = UserTab.objects.get(userid=userid)
        login_token = user.login_token
        
        # 排名
        def getRank(id, usersrank):
            for key, value in usersrank.items():
                if value['userid'] == id:
                    return key

        if token == login_token:

            # print(f'originscore = {user.totalscore}')
            user.totalscore += score
            # print(f'changescore = {user.totalscore}')
            user.save()

            usersByScore = UserTab.objects.all().order_by('-totalscore').values('userid')
            usersRank = {rank:id for rank, id in enumerate(usersByScore, start=1)}
            count = len(usersRank)
            rank = getRank(userid, usersRank)
            print(f'總人數: {count}; {userid}的排名:{rank}')

            # 回傳總分
            return JsonResponse({
                "status": "success",
                "feedback": "",
                "data":{
                        "totalscore": user.totalscore,
                        "count":count,
                        "rank":rank,
                    }
            }, safe=False)
        else:
            return JsonResponse({
                "status": "fail",
                "feedback": "noToken",
            }, safe=False)
        
    except Exception as e:
        print(traceback.format_exc())
        return JsonResponse({
                "status": str(e),
                "feedback": "",
                "data":{
                    "totalscore": "",
                    "count":"",
                    "rank":"",
                },
                }, safe=False)


    
    # return JsonResponse({
    #     "status": "success",
    #     "store": 100,
    #     "correct": True,
    #     "ranking": {
    #         "position": 5,
    #         "totalPlayers": 1
    #     }
    # }, safe=False)