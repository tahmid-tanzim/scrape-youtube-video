import requests
import os
# import json
# import csv
# from urllib.request import urlopen
from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.response import Response
from googleapiclient.discovery import build


# def getResponse(url):
#     response = None
#     try:
#         response = urlopen(url)
#     except Exception as ex:
#         print("Sorry!", ex)
#         return list()
#     else:
#         body = response.read()
#         return json.loads(body)
#     finally:
#         if response is not None:
#             response.close()

class VideoViewSet(viewsets.ViewSet):
    def __init__(self):
        api_service_name = "youtube"
        api_version = "v3"
        self.channel_id = 'UC_x5XG1OV2P6uZZ5FSM9Ttw'
        self.video_id = ('l-YO9CmaSUM', 'Be9UH1kXFDw', 'Zbm3hjPjQMk', 'BEtPCT7ZcE0')
        self.youtube = build(
            api_service_name,
            api_version,
            developerKey=settings.YOUTUBE_DATA_API_KEY
        )

    def retrieve(self, request, code=None):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        # request = self.youtube.search().list(
        #     part="snippet",
        #     channelId=self.channel_id,
        #     type='video',
        #     videoType='any',
        #     maxResults=50
        # )

        request = self.youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=",".join(self.video_id)
        )
        response = request.execute()
        print(response)

        response_body = dict()
        response_body['short_code'] = code
        response_body['name'] = 'Tahmid Tanzim'
        response_body['data'] = response
        return Response(response_body, status=status.HTTP_200_OK)
