from rest_framework import serializers
from .models import Mood, Feelog
from movies.models import Movie
from movies.serializers import MovieDetailSerializer

class FeelogListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Feelog
        fields = ('title','user', 'username')
        
class MovieFeelogSerializer(serializers.ModelSerializer):
    feelogs = FeelogListSerializer(many=True)
    class Meta:
      model = Movie
      fields = ('title','feelogs',)
      
class FeelogDetailSerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user.username', read_only=True)
  # movie = MovieDetailSerializer()
  class Meta:
    model = Feelog
    fields = ('title','content','username','user','created_at','movie','mood','like_users')
    read_only_fields = ('movie',)