from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # 영화 전체 조회 ('GET' : movies/)
    path('', views.movie_list, name='movie_list'),
    # 단일 영화 조회 ('GET' : movies/<movie_pk>)
    path('<movie_pk>/', views.movie, name='movie'),
    # 전체 장르 조회 ('GET' : movies/genres)
    path('all/genres/', views.genre_list, name='genre_list'),
    # 영화 찜하기
    path('<movie_pk>/save-movie/', views.save_movie, name='save_movie'),
    # 추천 영화 
    path('all/recommended/', views.recommended, name='recommended')
]
