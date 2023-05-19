from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from accounts.models import User
from .models import Feelog, Mood
from movies.models import Movie
from .serializers import FeelogListSerializer, FeelogDetailSerializer, MovieFeelogSerializer, MoodSerializer,FeelogMoodDetailSerializer

# 모든 feelog 조회(모든 내용 포함)
@api_view(['GET'])
def total_feelog_list(request):
  if request.method == 'GET':
        feelogs = get_list_or_404(Feelog)
        serializer = FeelogDetailSerializer(feelogs, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def user_feelog_list(request, username):
  if request.method == 'GET':
    user = get_object_or_404(User, username=username)
    feelogs = Feelog.objects.filter(user=user)
    serializer = FeelogDetailSerializer(feelogs, many=True)
    return Response(serializer.data)

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
    serializer = FeelogMoodDetailSerializer(feelog)
    return Response(serializer.data)
  elif request.method == 'DELETE':
    feelog = get_object_or_404(Feelog, pk=feelog_pk)
    feelog.delete()
    return Response({"DELETE": 'success'},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def mood_list(request):
  if request.method == 'GET':
    moods = get_list_or_404(Mood)
    serializer = MoodSerializer(moods, many=True)
    return Response(serializer.data)
