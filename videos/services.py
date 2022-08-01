import os
import googleapiclient.discovery
import googleapiclient.errors

from datetime import datetime
from django.conf import settings

from .models import Channel, Tag, Video

sample_youtube_channels = {
    'Google Developers': 'UC_x5XG1OV2P6uZZ5FSM9Ttw',
    'freeCodeCamp.org': 'UC8butISFwT-Wl7EV0hUK0BQ',
    'Dude Perfect': 'UCRijo3ddMTht_IHyNSNXpNQ',
    'Vox': 'UCLXo7UDZvByw2ixzpQCufnA',
    'mkbhd': 'UCBJycsmduvYEL83R_U4JriQ',
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
            reqChannels = self.youtube.channels().list(
                part='snippet,statistics',
                id=sample_youtube_channels['freeCodeCamp.org'],
                maxResults=50
            )

            resChannels = reqChannels.execute()
            channelObj = resChannels['items'][0]

            channel, isCreated = Channel.objects.update_or_create(
                channel_id=channelObj['id'],
                defaults={
                    'title': channelObj['snippet']['title'],
                    'description': channelObj['snippet']['description'],
                    'view_count': channelObj['statistics']['viewCount'],
                    'subscriber_count': channelObj['statistics']['subscriberCount'],
                    'video_count': channelObj['statistics']['videoCount'],
                    'published_at': channelObj['snippet']['publishedAt'],
                }
            )
            print('Success (channels.list)\n', resChannels)
            return channel
        except Exception as ex:
            print('ERROR (channels.list)', ex)
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
            print('Success (search.list)\n', resSearch)
            return videoIDs, nextPageToken,
        except Exception as ex:
            print('ERROR (search.list)', ex)
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
                print('Success (videos.list)\n', resVideos)
        except Exception as ex:
            print('ERROR (videos.list)', ex)

    def track_video(self):
        start = datetime.now()
        print("\nTracking Started -", start.strftime("%Y-%m-%d %H:%M:%S"), end='\n')

        channel = self.get_channel()
        if channel is not None:
            nextPageToken = ''
            # while nextPageToken is not None:
                # paginate video search list
            videoIDs, nextPageToken = self.search_videos(channel.channel_id, nextPageToken)
            # if len(videoIDs) == 0:
            #     break
            self.get_videos(channel, videoIDs)

        end = datetime.now()
        print("\nTracking End -", end.strftime("%Y-%m-%d %H:%M:%S"), end='\n')
