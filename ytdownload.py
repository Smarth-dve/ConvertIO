import pytube  
from pytube import YouTube  
print('fetching video url')
video_url = 'https://www.youtube.com/watch?v=UUheH1seQuE'
print('extracting video')
youtube = pytube.YouTube(video_url)  
print('streaming video')
print("Downloading")
video = YouTube(video_url).streams.get_highest_resolution().download(filename="outvideo.mp4")
print("Downloaded")