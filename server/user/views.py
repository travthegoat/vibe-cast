from djoser.views import UserViewSet as BaseUserViewSet
from .models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserSerializer

# Create your views here.
class UserViewSet(BaseUserViewSet):
    def get_queryset(self):
        username = self.request.query_params.get('username')
        if username:
            return User.objects.filter(username=username)
        return super().get_queryset()
    
class SocialViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=True, methods=['POST'])
    def follow(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        request.user.follow(user)
        return Response({'message': 'User followed successfully'})
    
    @action(detail=True, methods=['GET'])
    def followers(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        followers = user.followers.all()
        serializer = UserSerializer(followers, many=True)
        return Response({'count': user.get_followers_count(), 'results': serializer.data})
    
    @action(detail=True, methods=['GET'])
    def following(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        following = user.following.all()
        serializer = UserSerializer(following, many=True)
        return Response({'count': user.get_following_count(), 'results': serializer.data})
