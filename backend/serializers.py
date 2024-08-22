from backend.models import Player
from rest_framework import serializers

class RegisterRequestSerializer(serializers.Serializer):
    client_id = serializers.CharField()
    mail = serializers.CharField()
    password = serializers.CharField()

class AuthLoginRequestSerializer(serializers.Serializer):
    client_id = serializers.CharField()
    password = serializers.CharField()

class UploadRequestSerializer(serializers.Serializer):
    Authorization = serializers.CharField()
    file = serializers.CharField()
    mode = serializers.CharField()

class StartGameRequestSerializer(serializers.Serializer):
    Authorization = serializers.CharField()
    mode = serializers.CharField()

class SubmitGameRequestSerializer(serializers.Serializer):
    # Authorization = serializers.CharField()
    userid = serializers.CharField()
    score = serializers.IntegerField()
    token = serializers.CharField()
    

class PlayerSerializer(serializers.ModelSerializer):
     class Meta:
         model = Player
         fields = '__all__'


# class UserScoreSerializer(serializers.Serializer):
#     userid = serializers.CharField()         # 定義 userid 的類型
#     score = serializers.IntegerField()       # 定義 score 的類型

# class RankQuerySerializer(serializers.Serializer):
#     count = serializers.IntegerField()       # 整數類型的 count
#     rank = serializers.IntegerField()        # 整數類型的 rank
#     users = serializers.ListField(           # 包含物件的陣列
#         child=UserScoreSerializer()          # 使用嵌套的序列化器來定義每個物件
#     )



# class LineQuerySerializer(serializers.Serializer):
#     response_type = serializers.CharField()
#     client_id = serializers.CharField()
