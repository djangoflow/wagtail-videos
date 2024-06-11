from celery import current_app as app
from .signals import video_post_process
from wagtailvideos import get_video_model

@app.task()
def video_post_process_task(video_id: int) -> None:
    Video = get_video_model()
    video = Video.objects.get(id=video_id)
    video_post_process(video)
