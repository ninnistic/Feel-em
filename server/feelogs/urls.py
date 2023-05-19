from django.urls import path
from . import views

app_name = 'feelogs'
urlpatterns = [
    # # Feelog 전체 조회 ('GET')
    path('',views.total_feelog_list, name = 'total_feelog_list'),
    # # 한 유저가 작성한 Feelog 전체 조회('GET')
    path('<str:username>',views.user_feelog_list, name = 'user_feelog_list'),
    # # 한 영화에 대한 Feelog 전체 조회 ('GET')
    path('<int:movie_pk>/', views.feelog_list, name='feelog_list'),
    # # 상세 Feelog 조회 ('GET', 'DELETE', 'POST')
    path('<int:movie_pk>/<int:feelog_pk>/', views.feelog, name='feelog'),
    # # Mood 전체 조회 ('GET')
    path('moods', views.mood_list, name='mood_list'),
    # 
]
