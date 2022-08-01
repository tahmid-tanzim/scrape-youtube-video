from datetime import datetime
from django.db import models
# from django.utils.timezone import utc


class Channel(models.Model):
    channel_id = models.CharField(max_length=150)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    view_count = models.PositiveBigIntegerField()
    subscriber_count = models.PositiveBigIntegerField()
    video_count = models.PositiveBigIntegerField()
    published_at = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Channel - {self.channel_id}"

    class Meta:
        db_table = "channel"


class Tag(models.Model):
    value = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tag - {self.value}"

    class Meta:
        db_table = "tag"


class Video(models.Model):
    video_id = models.CharField(max_length=150)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    view_count = models.PositiveBigIntegerField()
    like_count = models.PositiveBigIntegerField()
    favorite_count = models.PositiveBigIntegerField()
    comment_count = models.PositiveBigIntegerField()
    published_at = models.DateTimeField(blank=True)
    performance_score = models.FloatField(default=0)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_elapsed_days(self):
        if self.published_at:
            now = datetime.utcnow()
            published_at = datetime.strptime(self.published_at, '%Y-%m-%dT%H:%M:%SZ')
            timediff = now - published_at
            return timediff.days
        return 0

    def save(self, *args, **kwargs):
        self.performance_score = int(self.view_count) / self.get_elapsed_days() * 100
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return f"Video - {self.video_id}"

    class Meta:
        db_table = "video"
