from threading import Timer
# from background_task import background
from django.conf import settings

from .services import VideoService


class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)


# @background(schedule=settings.TASKS_SCHEDULE)
def video_tracking_task():
    service = VideoService()
    service.track_video()


def start_background_task():
    timer = RepeatingTimer(settings.TASKS_REPEAT, video_tracking_task)
    timer.start()
    # TODO : if current_time exceed TASKS_REPEAT_UNTIL then call timer.cancel() 
