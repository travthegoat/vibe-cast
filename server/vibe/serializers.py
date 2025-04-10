from rest_framework import serializers
from .models import Vibe, Song
from user.serializers import UserSerializer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'spotify_id', 'cover_image']
        
class VibeSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    song = SongSerializer(read_only=True)
    
    class Meta:
        model = Vibe
        fields = ['id', 'author', 'mood', 'caption', 'song', 'created_at']
