from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User

class CustomUserSerializer(serializers.ModelSerializer):
    followings_count = serializers.IntegerField(source = 'followings.count')
    class Meta:
        model = User
        fields=('username','password','email','goal_of_month','followings','followings_count')


class CustomLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username','password')
