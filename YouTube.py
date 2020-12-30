# Modules
import re
from datetime import timedelta
from googleapiclient.discovery import build

# Api Key
API_KEY = 'AIzaSyCJSdKsZYS7UR13HO394SVsmhXWGCwFySY'

# Service Object
yt_object = build('youtube','v3',developerKey=API_KEY)

print("Enter the username of an Youtuber(Possible suggestions are 'PewDiePie):")

# YouTube username
username = input()

# Requests the basic channel information
request_channel = yt_object.channels().list(part='contentDetails, statistics',forUsername=username)

# Execute the request
response_channel = request_channel.execute()

# Acquire channel id
channel_id = response_channel['items'][0]["id"]

# Requests the playlist info
request_playlist = yt_object.playlists().list(part='contentDetails, snippet',channelId=channel_id)

# Execute the request
response_playlist = request_playlist.execute()

# Dict to store key: title of playlist value: playlist id
playlist_dict = {}

# Add playlist id's to dict
for playlist_id in response_playlist['items']:
    print(playlist_id['snippet']['title'],end=' | ')
    playlist_dict[playlist_id['snippet']['title']] = playlist_id['id']

print("\nEnter Title of Playlist you want to calculate the duration of:")

# Prompts user for title of an playlist
playlist_id = playlist_dict[input()]

# Requests the video info
request_videos = yt_object.playlistItems().list(part='contentDetails,snippet',playlistId=playlist_id)

# Execute the request
response_videos = request_videos.execute()

# List to store each video's id
video_ids = []

# Add to the empty list the video ids
for vid in response_videos['items']:
    video_ids.append(vid['contentDetails']['videoId'])

string = ','.join(video_ids)

# Set id equal to the string of video ids
request_video_id = yt_object.videos().list(part='contentDetails',id=string)

# Execute the request
response_video_id = request_video_id.execute()

# Regex
minutes_ex = re.compile(r'(\d+)M')
seconds_ex = re.compile(r'(\d+)S')
hours_ex = re.compile(r'(\d+)H')

video_dict = {}
times = []
total_seconds = 0
for vid_id in response_video_id['items']:
    minutes = minutes_ex.search(vid_id['contentDetails']['duration'])
    seconds = seconds_ex.search(vid_id['contentDetails']['duration'])
    hours = hours_ex.search(vid_id['contentDetails']['duration'])

    if hours:
        hours = int(hours.group(1))
    else:
        hours = 0
    
    if minutes:
        minutes = int(minutes.group(1))
    else:
        minutes = 0
    
    if seconds:
        seconds = int(seconds.group(1))
    else:
        seconds = 0

    video_time_seconds = timedelta(hours=hours,minutes= minutes,seconds= seconds).total_seconds()
    times.append(int(video_time_seconds)

    video_dict['title'] = 10

    total_seconds += video_time_seconds
      video_dict['title'] = 10


minutes, seconds = divmod(int(total_seconds),60)
hours, minutes = divmod(minutes,60)

print("{}H {}M {}S".format(hours, minutes,seconds))
print("Longest Video in {}".format(playlist_id))
print("Shortes Video in {}".format(playlist_id))

for i in response_videos['items']:
    print("\n")
    print(i)










