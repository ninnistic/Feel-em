from rest_framework import serializers
from .models import Movie, Genre

# create from here

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name',)

class MovieListSerializer(serializers.ModelSerializer): # movie 전체 데이터 목록을 가져올 serializer 생성
    class Meta:
        model = Movie
        fields = ('backdrop_path','title', 'overview', 'vote_average','poster_path','movie_num','id')

class MovieDetailSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields=('name',)
    genres = GenreSerializer(many=True, read_only = True)
    
    class Meta:
        model = Movie
        fields = '__all__'
    



