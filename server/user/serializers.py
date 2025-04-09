from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

class UserSerializer(BaseUserSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    vibes_count = serializers.SerializerMethodField()
    
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'display_name', 'profile_image', 'followers_count', 'following_count', 'vibes_count', 'joined_at']
        
    def get_followers_count(self, obj):
        return obj.get_followers_count()
    
    def get_following_count(self, obj):
        return obj.get_following_count()
    
    def get_vibes_count(self, obj):
        return obj.get_vibes_count()
    
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password']
        
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one number")
            
        if not any(char.islower() for char in value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter")
            
        return value
