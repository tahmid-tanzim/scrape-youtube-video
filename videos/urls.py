from django.conf import settings
from django.urls import path

from .views import VideoViewSet, TagViewSet, TestViewSet
from .tasks import video_tracking_task

urlpatterns = [
    # path("test/<str:code>", TestViewSet.as_view({
    #     "get": "retrieve"
    # })),

    path("tags", TagViewSet.as_view({
        "get": "list"
    })),

    path("videos/<str:order>/<str:tags>", VideoViewSet.as_view({
        "get": "list"
    })),
]

video_tracking_task(
    repeat=settings.TASKS_REPEAT,
    repeat_until=settings.TASKS_REPEAT_UNTIL
)
