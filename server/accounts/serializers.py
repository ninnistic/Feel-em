from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User,Profile
from movies.models import Genre, Movie

class UserSerializer(serializers.ModelSerializer):
    followings_count = serializers.IntegerField(source = 'followings.count')
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields=('name',)
    favorite_genre = GenreSerializer(many=True, read_only = True)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields=('title',)
    save_movies = MovieSerializer(many=True, read_only = True)

    class UserFollowSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields=('username',)
    followings = UserFollowSerializer(many=True, read_only = True)
    
    class UserProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields=('image',)
    profile_pic = UserProfileSerializer( read_only = True)
    class Meta:
        model = get_user_model()
        # fields=('username','password','email','goal_of_month','favorite_genre','followings','save_movies', 'genres')
        # read_only_fields = ('genres',)
        fields='__all__'

class UserSignUpSerializer(serializers.ModelSerializer):
    # followings_count = serializers.IntegerField(source = 'followings.count')
    
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields=('title',)
    save_movies = MovieSerializer(many=True, read_only = True)

    class UserFollowSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields=('username',)
    followings = UserFollowSerializer(many=True, read_only = True)
    
    class UserProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields=('image',)
    profile_pic = UserProfileSerializer( read_only = True)

    class Meta:
        model = get_user_model()
        # fields=('username','password','email','goal_of_month','favorite_genre','followings','save_movies', 'genres')
        # read_only_fields = ('genres',)
        fields='__all__'
