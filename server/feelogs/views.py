from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from accounts.models import User
from .models import Feelog, Mood
from movies.models import Movie
from .serializers import FeelogListSerializer, FeelogDetailSerializer, MovieFeelogSerializer, MoodSerializer,FeelogMoodDetailSerializer,FeelogMoodSerializer

# 모든 feelog 조회(모든 내용 포함)
@api_view(['GET'])
@permission_classes([AllowAny])
def total_feelog_list(request):
  if request.method == 'GET':
        feelogs = get_list_or_404(Feelog)
        serializer = FeelogDetailSerializer(feelogs, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def user_feelog_list(request, username):
  if request.method == 'GET':
    user = get_object_or_404(User, username=username)
    feelogs = Feelog.objects.filter(user=user)
    serializer = FeelogMoodSerializer(feelogs, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def feelogs_by_movie(request, movie_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
  if request.method == 'GET':
    serializer = MovieFeelogSerializer(movie)
    return Response(serializer.data)
  elif request.method == 'POST':
    # if request.user.is_authenticated:
    data = request.data.copy()
    data['user'] = request.user.pk
    serializer = FeelogDetailSerializer(data = data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(movie=movie)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
    

@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def feelog(request, feelog_pk):
  if request.method == 'GET':
    feelog = get_object_or_404(Feelog, pk=feelog_pk)
    serializer = FeelogMoodDetailSerializer(feelog)
    return Response(serializer.data)
  elif request.method == 'DELETE':
    feelog = get_object_or_404(Feelog, pk=feelog_pk)
    feelog.delete()
    return Response({"DELETE": 'success'},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([AllowAny])
def mood_list(request):
  if request.method == 'GET':
    moods = get_list_or_404(Mood)
    serializer = MoodSerializer(moods, many=True)
    return Response(serializer.data)

@api_view(['POST'])  
@permission_classes([IsAuthenticated])
def feeloglike(request,feelog_pk):
    if request.user.is_authenticated:
        feelog = get_object_or_404(Feelog, pk=feelog_pk)
        if request.user in feelog.like_users.all():
            feelog.like_users.remove(request.user)
            return Response({"Unfollow": 'success'})
        else:
            feelog.like_users.add(request.user)
            return Response({"follow": 'success'})