import requests
from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.response import Response


class VideoViewSet(viewsets.ViewSet):
    def retrieve(self, request, code=None):
        url = 'https://www.googleapis.com/youtube/v3/channels'
        params = {
            'part': 'snippet,contentDetails,statistics',
            'id': 'UC4JX40jDee_tINbkjycV4Sg',
            'key': settings.YOUTUBE_DATA_API_KEY
        }
        r = requests.get(url, params=params)
        print(r.text)
        response_body = dict()
        response_body['short_code'] = code
        response_body['name'] = 'Tahmid Tanzim'
        return Response(response_body, status=status.HTTP_200_OK)
