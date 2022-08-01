# import os
# from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.response import Response

# import googleapiclient.discovery
# import googleapiclient.errors

from .models import Channel, Tag, Video
from .services import VideoService
from .serializers import TagSerializer, VideoSerializer


class TagViewSet(viewsets.ViewSet):
    def list(self, request):
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VideoViewSet(viewsets.ViewSet):
    def list(self, request, order='DESC', tags=''):
        # video = Video.objects.filter(tags__in=[tags]).order_by(f'{"-" if order == "DESC" else ""}performance_score')
        video = Video.objects.all().order_by(f'{"-" if order == "DESC" else ""}performance_score')
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TestViewSet(viewsets.ViewSet):
    def __init__(self):
        self.service = VideoService()
        # self.channels = {
        #     'Google Developers': 'UC_x5XG1OV2P6uZZ5FSM9Ttw',
        #     'freeCodeCamp.org': 'UC8butISFwT-Wl7EV0hUK0BQ',
        #     'Dude Perfect': 'UCRijo3ddMTht_IHyNSNXpNQ',
        #     'Vox': 'UCLXo7UDZvByw2ixzpQCufnA',
        #     'mkbhd': 'UCBJycsmduvYEL83R_U4JriQ',
        # }
        #
        # self.video_id = ('l-YO9CmaSUM', 'Be9UH1kXFDw', 'Zbm3hjPjQMk', 'BEtPCT7ZcE0',)
        # self.videoIDs = None
        # self.youtube = googleapiclient.discovery.build(
        #     settings.SERVICE['name'],
        #     settings.SERVICE['version'],
        #     developerKey=settings.SERVICE['key']
        # )

    # def scrape_youtube_videos(self, request):
    #     track_video_statistics(repeat=settings.TASKS_REPEAT, repeat_until=settings.TASKS_REPEAT_UNTIL)
    #     return Response({'message': 'Success'}, status=status.HTTP_200_OK)

    def retrieve(self, request, code=None):
        # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        try:
            # """
            # Get YouTube Channel
            # """
            # requestChannels = self.youtube.channels().list(
            #     part='snippet,statistics',
            #     id=self.channels['freeCodeCamp.org'],
            #     maxResults=50
            # )
            #
            # responseChannels = requestChannels.execute()
            # channelObj = responseChannels['items'][0]
            # # print('Get YouTube Channel\n', channelObj, end='\n')
            #
            # channel, isChannelCreated = Channel.objects.update_or_create(
            #     channel_id=channelObj['id'],
            #     defaults={
            #         'title': channelObj['snippet']['title'],
            #         'description': channelObj['snippet']['description'],
            #         'view_count': channelObj['statistics']['viewCount'],
            #         'subscriber_count': channelObj['statistics']['subscriberCount'],
            #         'video_count': channelObj['statistics']['videoCount'],
            #         'published_at': channelObj['snippet']['publishedAt'],
            #     }
            # )
            #
            # """
            # Search YouTube videos by Channel ID
            # """
            # requestSearch = self.youtube.search().list(
            #     part='snippet',
            #     channelId=channel.channel_id,
            #     type='video',
            #     videoType='any',
            #     order='viewCount',
            #     maxResults=50
            # )
            #
            # responseSearch = requestSearch.execute()
            # self.videoIDs = set(map(lambda item: item['id']['videoId'], responseSearch['items']))
            #
            # """
            # Get YouTube Videos
            # """
            # requestVideos = self.youtube.videos().list(
            #     part='snippet,statistics',
            #     id=','.join(self.videoIDs)
            # )
            #
            # responseVideos = requestVideos.execute()
            # print(responseVideos)
            # for videoObj in responseVideos['items']:
            #     video, isVideoCreated = Video.objects.update_or_create(
            #         video_id=videoObj['id'],
            #         channel=channel,
            #         defaults={
            #             'title': videoObj['snippet']['title'],
            #             'description': videoObj['snippet']['description'],
            #             'view_count': videoObj['statistics']['viewCount'],
            #             'like_count': videoObj['statistics']['likeCount'],
            #             'favorite_count': videoObj['statistics']['favoriteCount'],
            #             'comment_count': videoObj['statistics']['commentCount'],
            #             'published_at': videoObj['snippet']['publishedAt'],
            #         }
            #     )
            #
            #     if isVideoCreated and 'tags' in videoObj['snippet']:
            #         tags = []
            #         for value in videoObj['snippet']['tags']:
            #             tag, _ = Tag.objects.get_or_create(value=value)
            #             tags.append(tag)
            #         video.tags.add(*tags)
            #         video.save()
            #         print(f'Video {video.video_id} tags added')
            #     print('SAVE YouTube Video\n', video, end='\n')

            self.service.track_video()
            response_body = dict()
            response_body['short_code'] = code
            response_body['name'] = 'Tahmid Tanzim'
            return Response(response_body, status=status.HTTP_200_OK)
        except Exception as ex:
            print('-- ERROR --')
            print(ex)
            print('-- ERROR --')
            return Response({'message': 'ERROR'}, status=status.HTTP_400_BAD_REQUEST)
