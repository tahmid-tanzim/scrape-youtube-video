from background_task import background
from django.conf import settings

from .services import VideoService


@background(schedule=settings.TASKS_SCHEDULE)
def track_video_statistics():
    service = VideoService()
    service.track_video()
