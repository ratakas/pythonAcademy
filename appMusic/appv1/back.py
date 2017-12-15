""" Pull All Youtube Videos from a Playlist """
import json


from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


DEVELOPER_KEY = "AIzaSyBDwBDY9lQ62RwMmlDhs8Djw6YlBxynZrs"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def fetch_all_youtube_videos(playlistId):
    """
    Fetches a playlist of videos from youtube
    We splice the results together in no particular order

    Parameters:
        parm1 - (string) playlistId
    Returns:
        playListItem Dict
    """
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    res = youtube.playlistItems().list(
    part="snippet",
    playlistId=playlistId,
    maxResults="50"
    ).execute()

    nextPageToken = res.get('nextPageToken')
    while ('nextPageToken' in res):
        nextPage = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlistId,
        maxResults="50",
        pageToken=nextPageToken
        ).execute()
        res['items'] = res['items'] + nextPage['items']

        if 'nextPageToken' not in nextPage:
            res.pop('nextPageToken', None)
        else:
            nextPageToken = nextPage['nextPageToken']

    return res

if __name__ == '__main__':
  # comedy central playlist, has 332 video
  # https://www.youtube.com/watch?v=tJDLdxYKh3k&list=PLD7nPL1U-R5rDpeH95XsK0qwJHLTS3tNT
  #videos = fetch_all_youtube_videos("PLAEnFHFz2ruTSyCiMXF3JLiGW_FyMH6y2")
  videos = fetch_all_youtube_videos("PLAEnFHFz2ruTI-21T0wrZrQWY5y49l8Ij")

#print(videos)
  data = json.dumps(videos)
  #print ('JSON:', data_string)
  jsonObject = json.loads(data["items"])

  for key,value in jsonObject.items():
    #value = jsonObject[key]
    #print("The key and value are ({}) = ({})".format(key, value))
    #print(jsonObject)
    print(key)