from backend.models import Player
from rest_framework import serializers

class AuthLoginRequestSerializer(serializers.Serializer):
    lineUserId = serializers.CharField()
    lineAccessToken = serializers.CharField()

class UploadRequestSerializer(serializers.Serializer):
    Authorization = serializers.CharField()
    file = serializers.ImageField()
    mode = serializers.CharField()

class StartGameRequestSerializer(serializers.Serializer):
    Authorization = serializers.CharField()
    mode = serializers.CharField()

class SubmitGameRequestSerializer(serializers.Serializer):
    Authorization = serializers.CharField()
    gameId = serializers.CharField()
    recognizedWord = serializers.CharField()
    timeSpent =  serializers.FloatField()

class PlayerSerializer(serializers.ModelSerializer):
     class Meta:
         model = Player
         fields = '__all__'