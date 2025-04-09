from djoser.views import UserViewSet as BaseUserViewSet
from .models import User

# Create your views here.
class UserViewSet(BaseUserViewSet):
    def get_queryset(self):
        username = self.request.query_params.get('username')
        if username:
            return User.objects.filter(username=username)
        return super().get_queryset()
    
