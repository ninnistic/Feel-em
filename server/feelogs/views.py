from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Feelog, Mood
from movies.models import Movie
from .serializers import FeelogListSerializer, FeelogDetailSerializer, MovieFeelogSerializer

@api_view(['GET','POST'])
def feelog_list(request, movie_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
  if request.method == 'GET':
    serializer = MovieFeelogSerializer(movie)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = FeelogDetailSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(movie=movie)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  
    

@api_view(['GET','DELETE']) 
def feelog(request, movie_pk, feelog_pk):
  if request.method == 'GET':
    movie = get_object_or_404(Movie, pk=movie_pk)
    feelog = get_object_or_404(Feelog, pk=feelog_pk)
    serializer = FeelogDetailSerializer(feelog)
    return Response(serializer.data)
  elif request.method == 'DELETE':
    feelog = get_object_or_404(Feelog, pk=feelog_pk)
    feelog.delete()
    return Response({"DELETE": 'suceshvefb'},status=status.HTTP_204_NO_CONTENT)

