# from django.conf import settings
from django.urls import path

from .views import VideoViewSet, TagViewSet
from .tasks import video_tracking_task, start_background_task

urlpatterns = [
    path("tags", TagViewSet.as_view({
        "get": "list"
    })),
    path("videos", VideoViewSet.as_view({
        "get": "list"
    })),
]

# video_tracking_task(
#     repeat=settings.TASKS_REPEAT,
#     repeat_until=settings.TASKS_REPEAT_UNTIL
# )

# start_background_task()