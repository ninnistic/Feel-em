from django.urls import path
from . import views

app_name = 'feelogs'
urlpatterns = [
    # # Feelog 전체 조회 ('GET')
    # path('', views.feelog_list, name='feelog_list'),
    # # 상세 Feelog 조회 ('GET', 'DELETE', 'POST')
    # path('<feelog_pk>', views.feelog, name='feelog'),
    # # Mood 전체 조회 ('GET')
    # path('moods', views.mood_list, name='mood_list'),

]
