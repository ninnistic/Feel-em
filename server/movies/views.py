from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Genre
from .serializers import MovieDetailSerializer,MovieListSerializer, GenreListSerializer
# Create your views here.

@api_view(['GET'])
def genre_list(request):
    if request.method == 'GET':
        genres = get_list_or_404(Genre)
        serializer = GenreListSerializer(genres, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])        
def movie(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    
@api_view(['POST'])  
def likemovie(request,movie_pk):
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