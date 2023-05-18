from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('logout',views.logout, name='logout'),
    path('<str:username>',views.profile, name='profile'),
    path('<str:username>/follow',views.follow, name='follow')
]
