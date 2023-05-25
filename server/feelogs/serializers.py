from rest_framework import serializers
from .models import Mood, Feelog
from movies.models import Movie
from movies.serializers import MovieDetailSerializer
from collections import Counter
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
  class Meta:
    model = Feelog
    fields = ('title','content','username','user','created_at','movie','mood', 'id','like_users',)
    read_only_fields = ('movie',)
    
    
class FeelogMoodSerializer(serializers.ModelSerializer):
    class MoodSerializer(serializers.ModelSerializer):
        title_count = serializers.SerializerMethodField()

        class Meta:
            model = Mood
            fields = ('id', 'title', 'title_count')

        def get_title_count(self, obj):
            feelog_moods = self.context.get('feelog_moods', {})
            user_id = self.context.get('user_id')  # 유저 ID를 가져옵니다.
            title = obj.title
            user_feelogs = feelog_moods.get(user_id, [])  # 해당 유저의 Feelog 목록을 가져옵니다.
            mood_titles = [feelog.mood.title for feelog in user_feelogs]
            title_counts = Counter(mood_titles)
            return title_counts.get(title, 0)

    username = serializers.CharField(source='user.username', read_only=True)
    mood = MoodSerializer(read_only=True, many=False)

    class Meta:
        model = Feelog
        fields = ('title', 'content', 'username', 'user', 'created_at', 'movie', 'mood', 'id', 'like_users',)
        read_only_fields = ('movie',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_id = instance.user.id  # Feelog 객체의 user ID를 가져옵니다.
        representation['mood']['title_count'] = self.calculate_title_count(user_id, representation['mood']['title'])
        return representation

    def calculate_title_count(self, user_id, title):
        user_feelogs = Feelog.objects.filter(user_id=user_id)
        mood_titles = [feelog.mood.title for feelog in user_feelogs]
        title_counts = Counter(mood_titles)
        return title_counts.get(title, 0)



      
      
    
  
class FeelogMoodDetailSerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user.username', read_only=True)
  # like_users_count = serializers.IntegerField(source = 'like_users.count', blank=True)
  # movie = MovieDetailSerializer()

  class Meta:
    model = Feelog
    fields = ('title','content','username','user','created_at','movie','mood','like_users', 'id',)
    read_only_fields = ('movie',)
    
    
class MoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mood
    fields = '__all__'