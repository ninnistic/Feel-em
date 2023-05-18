from rest_framework import serializers
from .models import Movie, Genre

# create from here

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)

class MovieListSerializer(serializers.ModelSerializer): # movie 전체 데이터 목록을 가져올 serializer 생성
    # genres = GenreListSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('title', 'overview', 'vote_average',)


    



