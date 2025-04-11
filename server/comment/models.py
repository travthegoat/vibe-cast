from django.db import models
from uuid import uuid4
from user.models import User
from vibe.models import Vibe

# Create your models here.
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    vibe = models.ForeignKey(Vibe, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.username} - {self.vibe.song.title}"
    
