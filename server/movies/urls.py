from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # 영화 전체 조회 ('GET' : movies/)
    # path('', views.movie_list, name='movie_list' ),
    # 단일 영화 조회 ('GET' : movies/<movie_pk>)
    # path('<movie_pk>', views.movie, name='movie'),
    # 전체 장르 조회 ('GET' : movies/genres)
    # path('genres', views.genres, name='genres')
]
