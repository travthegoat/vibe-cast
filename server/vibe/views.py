from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response

from comment.serializers import CommentSerializer
from user.serializers import UserSerializer
from .models import Vibe, Song
from .permissions import IsVibeOwner
from .serializers import VibeSerializer, SongSerializer

class VibeViewSet(viewsets.ModelViewSet):
    queryset = Vibe.objects.all()
    serializer_class = VibeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['mood', 'author']
    search_fields = ('song__title', 'song__artist')
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsVibeOwner()]
        return super().get_permissions()
    
    def get_queryset(self):
        if self.action == 'list' and self.request.query_params.get('random') == 'true':
            return Vibe.objects.all().order_by('?')
        return super().get_queryset()
    
    def create(self, request, *args, **kwargs):
        song_data = request.data.pop('song')
        song, created = Song.objects.get_or_create(
            spotify_id=song_data['spotify_id'],
            title=song_data['title'],
            artist=song_data['artist'],
            cover_image=song_data['cover_image']
        )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user, song=song)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        vibe = get_object_or_404(Vibe, id=pk)
        success = vibe.like(request.user)
        if success:
            return Response({ 'message': "Vibe liked successfully!" }, status=status.HTTP_200_OK)
        else:
            return Response({ 'message': "Vibe disliked successfully!" }, status=status.HTTP_200_OK)
        
    @action(detail=True, methods=['GET'])
    def likes(self, request, pk=None):
        vibe = get_object_or_404(Vibe, id=pk)
        likes = vibe.likes.all()
        serializer = UserSerializer(likes, many=True)
        return Response({ 'count': vibe.get_likes_count(), 'results': serializer.data }, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def comments(self, request, pk=None):
        vibe = get_object_or_404(Vibe, id=pk)
        comments = vibe.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response({ 'count': comments.count(), 'results': serializer.data}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['POST'])
    def comment(self, request, pk=None):
        vibe = get_object_or_404(Vibe, id=pk)
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user, vibe=vibe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
