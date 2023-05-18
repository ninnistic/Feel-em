from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User
from .serializers import CustomUserSerializer, CustomLoginSerializer
from django.contrib.auth import get_user, authenticate
from django.contrib.auth.models import AnonymousUser
from django.views.decorators.csrf import csrf_exempt

# CSRF 없이는 안된다...아래 처럼 전달 동시에 같이 해줘야 함.
# $.ajax({
#     // ...
#     headers: {
#         "X-CSRFToken": getCookie("csrftoken")  // CSRF 토큰 가져오기
#     },
#     // ...
# });
@csrf_exempt
@api_view(['POST'])
def signup(request):
    if request.method =='POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            auth_login(request, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        
@api_view(['POST'])
def signin(request):
    if request.method =='POST':
        if request.user.is_authenticated:
            return Response({"Login": 'success'},status=status.HTTP_202_ACCEPTED)

        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return Response({"Login": 'success'},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"Login": 'failed'},status=status.HTTP_401_UNAUTHORIZED)
        
@api_view(['GET'])     
def logout(request):
    if request.method =='GET':
        auth_logout(request)
        return Response({"Logout": 'success'})
    
@api_view(['GET','PUT','DELETE'])   
def profile(request,username):
    user = get_object_or_404(User, username=username)
    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomUserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method =='DELETE':
        user.delete()
        return Response({"DELETE": 'success'},status = status.HTTP_204_NO_CONTENT)

@api_view(['POST'])  
def follow(request,username):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=username)
        if request.user in user.followings.all():
            user.followings.remove(request.user)
            return Response({"Unfollow": 'success'})
        else:
            user.followings.add(request.user)
            return Response({"follow": 'success'})