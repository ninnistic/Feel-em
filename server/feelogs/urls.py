from django.urls import path
from . import views

app_name = 'feelogs'
urlpatterns = [
    # # Feelog 전체 조회 ('GET')
    path('<int:movie_pk>/', views.feelog_list, name='feelog_list'),
    # # 상세 Feelog 조회 ('GET', 'DELETE', 'POST')
    path('<int:movie_pk>/<int:feelog_pk>/', views.feelog, name='feelog'),
    # # Mood 전체 조회 ('GET')
    path('moods', views.mood_list, name='mood_list'),
    # 
]
