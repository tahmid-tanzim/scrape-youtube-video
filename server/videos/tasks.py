from background_task import background
from django.conf import settings

from .services import VideoService


@background(schedule=settings.TASKS_SCHEDULE)
def video_tracking_task():
    service = VideoService()
    service.track_video()
