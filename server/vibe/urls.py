from rest_framework_nested import routers
from .views import VibeViewSet

router = routers.DefaultRouter()
router.register(r'vibes', VibeViewSet, basename='vibes')

urlpatterns = router.urls

