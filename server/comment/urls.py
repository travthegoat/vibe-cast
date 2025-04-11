from django.urls import path
from .views import CommentUpdateDestroyView

urlpatterns = [
    path('<uuid:pk>/', CommentUpdateDestroyView.as_view(), name='comment-update-destroy'),
]
