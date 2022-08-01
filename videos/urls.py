from django.conf import settings
from django.urls import path

from .views import VideoViewSet
from .tasks import track_video_statistics

urlpatterns = [
    path("videos/<str:code>", VideoViewSet.as_view({
        "get": "retrieve"
    })),
    # path("scrape-videos", VideoViewSet.as_view({
    #     "get": "scrape_youtube_videos"
    # })),
]

track_video_statistics(repeat=settings.TASKS_REPEAT, repeat_until=settings.TASKS_REPEAT_UNTIL)
