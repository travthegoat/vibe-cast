from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    display_name = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    followers = models.ManyToManyField(
        'self',
        related_name='following',
        symmetrical=False,
        blank=True
    )
    
    def follow(self, user):
        if self == user:
            raise ValueError("You cannot follow yourself")
        
        if user in self.following.all():
            self.unfollow(user)
            return
        
        self.following.add(user)
    
    def unfollow(self, user):
        self.following.remove(user)
    
    def get_followers_count(self):
        return self.followers.count()
    
    def get_following_count(self):
        return self.following.count()
    
    def get_vibes_count(self):
        return self.vibes.count()
    
