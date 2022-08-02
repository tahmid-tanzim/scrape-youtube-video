from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Tag, Video
from .serializers import TagSerializer, VideoSerializer


class TagViewSet(viewsets.ViewSet):
    def list(self, request):
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VideoViewSet(viewsets.ViewSet):
    def list(self, request):
        order_type = 'performance_score'
        if request.query_params.get('score_order', 'DESC') == 'DESC':
            order_type = '-' + order_type

        tags = request.query_params.get('tags', None)
        if tags is not None:
            try:
                tags = list(map(int, tags.split(',')))
                video = Video.objects.filter(tags__in=tags).distinct().order_by(order_type)
            except ValueError:
                return Response({'message': 'Sorry! Invalid tags'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            video = Video.objects.all().order_by(order_type)

        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

