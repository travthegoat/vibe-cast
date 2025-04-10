from rest_framework_nested import routers
from .views import SocialViewSet

router = routers.DefaultRouter()
router.register(r'users', SocialViewSet, basename='users')

urlpatterns = router.urls