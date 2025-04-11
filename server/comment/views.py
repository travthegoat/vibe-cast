from rest_framework import generics, permissions, status
from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsCommentOwner
from rest_framework.response import Response

# Create your views here.
class CommentUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsCommentOwner]
    
    def get(self, request, *args, **kwargs):
        return Response({ "message": "Method Not Allowed" }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
