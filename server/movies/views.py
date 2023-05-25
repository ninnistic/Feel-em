from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Genre
from accounts.models import User 
from .serializers import MovieDetailSerializer,MovieListSerializer, GenreListSerializer
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def genre_list(request):
    if request.method == 'GET':
        genres = get_list_or_404(Genre)
        serializer = GenreListSerializer(genres, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([AllowAny])      
def movie(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_movie(request,movie_pk):
    # if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            movie = get_object_or_404(Movie, pk=movie_pk)
            if movie in user.save_movies.all():
                user.save_movies.remove(movie)
                return Response({"Unllike": 'success'})
            else:
                user.save_movies.add(movie)
                return Response({"like": 'success'})
            

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommended(request):
    user = request.user
    user_likes = user.favorite_genre.all()
    movies = Movie.objects.filter(genres__in=user_likes)[:15]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)