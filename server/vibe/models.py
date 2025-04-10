from django.db import models
from uuid import uuid4
from user.models import User

# Create your models here.
class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    spotify_id = models.CharField(max_length=255, unique=True)
    cover_image = models.URLField()
    
    def __str__(self):
        return f"{self.title} - {self.artist}"

class Vibe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vibes')
    mood = models.CharField(max_length=100)
    caption = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.username} - {self.mood} - {self.song.title}"
