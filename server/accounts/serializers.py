from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # followings_count = serializers.IntegerField(source = 'followings.count')
    class Meta:
        model = get_user_model()
        fields=('username','password','email','goal_of_month','favorite_genre','followings','save_movies')

