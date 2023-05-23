from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, UserSignUpSerializer
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from .models import User
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# 서버가 요청한 요구사항 해결하기  -> 클라이언트에는 3개의 값이 넘어감(username, password, passwordConfirm)
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    # 아이디, 비밀번호, 비밀번호 확인
    password = request.data.get('password')       
    password_confirm = request.data.get('passwordConfirm')
    # 비밀번호 일치 여부 확인
    if password != password_confirm:
        return Response({'error': "비밀번호가 일치하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSignUpSerializer(data=request.data) # serializer로 비밀번호를 가져옴.
    # 유효성 검사 진행
    if serializer.is_valid(raise_exception=True):
        # 여기까지 들어왔다는 것은 비밀 번호가 유효하다는 것.
        user = serializer.save()
        # 비밀 번호를 hash해서 저장함.
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) # 완료된 데이터를 담아서 전송(hash된 비밀번호)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])   
def profile(request,username):
    user = get_object_or_404(User, username=username)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method =='DELETE':
        user.delete()
        return Response({"DELETE": 'success'},status = status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def follow(request,username):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=username)
        if user in request.user.followings.all():
            request.user.followings.remove(user)
            return Response({"Unfollow": 'success'})
        else:
            request.user.followings.add(user)
            return Response({"follow": 'success'})

@api_view(['POST'])
@permission_classes([AllowAny])
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
@permission_classes([IsAuthenticated])   
def logout(request):
    if request.method =='GET':
        auth_logout(request)
        return Response({"Logout": 'success'})
    
    
    
    
    
    
    
    
    
    
    
    

# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from django.shortcuts import get_object_or_404, get_list_or_404
# from django.contrib.auth import login as auth_login
# from django.contrib.auth import logout as auth_logout
# from .models import User
# from .serializers import CustomUserSerializer, CustomLoginSerializer
# from django.contrib.auth import get_user, authenticate
# from django.contrib.auth.models import AnonymousUser
# from django.views.decorators.csrf import csrf_exempt

# # CSRF 없이는 안된다...아래 처럼 전달 동시에 같이 해줘야 함.
# # $.ajax({
# #     // ...
# #     headers: {
# #         "X-CSRFToken": getCookie("csrftoken")  // CSRF 토큰 가져오기
# #     },
# #     // ...
# # });
# @csrf_exempt
# @api_view(['POST'])
# def signup(request):
#     if request.method =='POST':
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.save()
#             auth_login(request, user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

        
# @api_view(['POST'])
# def signin(request):
#     if request.method =='POST':
#         if request.user.is_authenticated:
#             return Response({"Login": 'success'},status=status.HTTP_202_ACCEPTED)

#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             auth_login(request, user)
#             return Response({"Login": 'success'},status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response({"Login": 'failed'},status=status.HTTP_401_UNAUTHORIZED)
        
# @api_view(['GET'])     
# def logout(request):
#     if request.method =='GET':
#         auth_logout(request)
#         return Response({"Logout": 'success'})
    
# @api_view(['GET','PUT','DELETE'])   
# def profile(request,username):
#     user = get_object_or_404(User, username=username)
#     if request.method == 'GET':
#         serializer = CustomUserSerializer(user)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CustomUserSerializer(user,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method =='DELETE':
#         user.delete()
#         return Response({"DELETE": 'success'},status = status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])  
# def follow(request,username):
#     if request.user.is_authenticated:
#         user = get_object_or_404(User, username=username)
#         if request.user in user.followings.all():
#             user.followings.remove(request.user)
#             return Response({"Unfollow": 'success'})
#         else:
#             user.followings.add(request.user)
#             return Response({"follow": 'success'})