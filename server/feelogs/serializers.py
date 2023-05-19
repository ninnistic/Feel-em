from rest_framework import serializers
from .models import Mood, Feelog
from movies.models import Movie
from movies.serializers import MovieDetailSerializer

# class TotalFeeologSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Feelog
#         fields = '__all__'


class FeelogListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Feelog
        fields = '__all__'
        
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
    fields = ('title','content','username','user','created_at','movie','mood')
    read_only_fields = ('movie',)

class FeelogMoodDetailSerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user.username', read_only=True)
  like_users_count = serializers.IntegerField(source = 'like_users.count')
  # movie = MovieDetailSerializer()
  class Meta:
    model = Feelog
    fields = ('title','content','username','user','created_at','movie','mood','like_users','like_users_count')
    read_only_fields = ('movie',)
    
class MoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mood
    fields = '__all__'