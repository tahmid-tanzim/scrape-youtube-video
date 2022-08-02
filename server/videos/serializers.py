from rest_framework import serializers
from .models import Video, Tag, Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('channel_id', 'title', 'subscriber_count', 'video_count', 'published_at',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'value',)


class VideoSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer(many=False)

    class Meta:
        model = Video
        exclude = ('tags', 'created_at', 'updated_at',)
