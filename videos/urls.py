from django.urls import path
from .views import VideoViewSet

urlpatterns = [
   path("videos/<str:code>", VideoViewSet.as_view({
        "get": "retrieve"
    })),
]