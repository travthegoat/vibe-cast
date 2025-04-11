from rest_framework import serializers
from .models import Comment
from user.serializers import UserSerializer
from vibe.serializers import VibeSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    vibe = VibeSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'vibe', 'content', 'created_at']
