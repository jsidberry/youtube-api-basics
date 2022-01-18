from googleapiclient.discovery import build
import os

api_key = os.environ.get('GOOGLE_DEV_API_KEY')
username = os.environ.get('GOOGLE_DEV_USERNAME')

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    forUsername=username
)

response = request.execute()

print(response)
