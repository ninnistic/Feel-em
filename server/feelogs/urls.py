from django.urls import path
from . import views

app_name = 'feelogs'
urlpatterns = [
    # # Feelog 전체 조회 ('GET')
    path('',views.total_feelog_list, name = 'total_feelog_list'),
    # # 한 유저가 작성한 Feelog 전체 조회('GET')
    path('<str:username>',views.user_feelog_list, name = 'user_feelog_list'),
    # # 한 영화에 대한 Feelog 전체 조회 및 작성 ('GET', 'POST')
    # feelog_pk에서 movie_pk는 필요가 없음 -> 왜냐하면 이미 feelog_pk가 어차피 원래 unique한 값이기 때문임
    # 그러나 feelog_pk를 쓰면 movie_pk랑 값이 같아지기 때문에, 구별하기 위해서 by-movie를 붙임. 
    path('by-movie/<int:movie_pk>/', views.feelogs_by_movie, name='feelogs_by_movie'),
    # # 상세 Feelog 조회 ('GET', 'DELETE', )
    path('<int:feelog_pk>/', views.feelog, name='feelog'),
    # # Mood 전체 조회 ('GET')
    path('moods/', views.mood_list, name='mood_list'),
    path('<int:feelog_pk>/like/', views.feeloglike, name='feeloglike'),
    # 
]
