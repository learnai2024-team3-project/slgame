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


# class LineQuerySerializer(serializers.Serializer):
#     response_type = serializers.CharField()
#     client_id = serializers.CharField()
