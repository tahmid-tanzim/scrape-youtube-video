import os
import googleapiclient.discovery
import googleapiclient.errors

from datetime import datetime
from django.conf import settings

from .models import Channel, Tag, Video

sample_youtube_channels = {
    'freeCodeCamp.org': 'UC8butISFwT-Wl7EV0hUK0BQ',
    'Dude Perfect': 'UCRijo3ddMTht_IHyNSNXpNQ',
}


class VideoService:
    def __init__(self):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        self.youtube = googleapiclient.discovery.build(
            settings.SERVICE['name'],
            settings.SERVICE['version'],
            developerKey=settings.SERVICE['key']
        )

    def get_channel(self):
        try:
            channel = Channel.objects.get(channel_id=sample_youtube_channels['freeCodeCamp.org'])
            return channel
        except Channel.DoesNotExist:
            reqChannels = self.youtube.channels().list(
                part='snippet,statistics',
                id=sample_youtube_channels['freeCodeCamp.org'],
                maxResults=50
            )

            resChannels = reqChannels.execute()
            channelObj = resChannels['items'][0]

            channel = Channel.objects.create(
                channel_id=channelObj['id'],
                title=channelObj['snippet']['title'],
                description=channelObj['snippet']['description'],
                view_count=channelObj['statistics']['viewCount'],
                subscriber_count=channelObj['statistics']['subscriberCount'],
                video_count=channelObj['statistics']['videoCount'],
                published_at=channelObj['snippet']['publishedAt']
            )
            print('\nSuccess in channels.list\n', resChannels)
            return channel
        except Exception as ex:
            print('\nERROR in channels.list', ex)
            return None

    def search_videos(self, channelId, pageToken=''):
        try:
            reqSearch = self.youtube.search().list(
                part='snippet',
                channelId=channelId,
                type='video',
                videoType='any',
                order='viewCount',
                pageToken=pageToken,
                maxResults=50
            )

            resSearch = reqSearch.execute()
            nextPageToken = resSearch.get('nextPageToken', None)
            videoIDs = set(map(lambda item: item['id']['videoId'], resSearch['items']))
            print('\nSuccess in search.list by channel_id\n', videoIDs)
            return videoIDs, nextPageToken,
        except Exception as ex:
            print('\nERROR in search.list by channel_id', ex)
            return set(), None,

    def get_videos(self, channel, videoIDs):
        try:
            reqVideos = self.youtube.videos().list(
                part='snippet,statistics',
                id=','.join(videoIDs)
            )

            resVideos = reqVideos.execute()

            for videoObj in resVideos['items']:
                video, isCreated = Video.objects.update_or_create(
                    video_id=videoObj['id'],
                    channel=channel,
                    defaults={
                        'title': videoObj['snippet']['title'],
                        'description': videoObj['snippet']['description'],
                        'view_count': videoObj['statistics']['viewCount'],
                        'like_count': videoObj['statistics']['likeCount'],
                        'favorite_count': videoObj['statistics']['favoriteCount'],
                        'comment_count': videoObj['statistics']['commentCount'],
                        'published_at': videoObj['snippet']['publishedAt'],
                    }
                )

                if isCreated and 'tags' in videoObj['snippet']:
                    tags = []
                    for value in videoObj['snippet']['tags']:
                        tag, _ = Tag.objects.get_or_create(value=value)
                        tags.append(tag)
                    video.tags.add(*tags)
                    video.save()
            print('\nSuccess in videos.list\n', resVideos['etag'])
            return True
        except Exception as ex:
            print('\nERROR in videos.list', ex)
            return False

    def track_video(self):
        start = datetime.now()
        print("\nVideo Tracking Started -", start.strftime("%Y-%m-%d %H:%M:%S"), end='\n')

        channel = self.get_channel()
        if channel is not None:
            # TODO : request quotaExceeded due to search pagination
            """
            # nextPageToken = ''
            # while nextPageToken is not None:
            #     # paginate video search list
            #     videoIDs, nextPageToken = self.search_videos(channel.channel_id, nextPageToken)
            #     if len(videoIDs) == 0:
            #         break
            #     success = self.get_videos(channel, videoIDs)
            #     if not success:
            #         break
            #     print(f'NEXT Page Token - {nextPageToken}')
            """

            videoIDs, _ = self.search_videos(channel.channel_id)
            if len(videoIDs) > 0:
                self.get_videos(channel, videoIDs)

        end = datetime.now()
        print("\nVideo Tracking End -", end.strftime("%Y-%m-%d %H:%M:%S"), end='\n')
