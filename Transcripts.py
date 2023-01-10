from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
from pydub import AudioSegment
import pydub
from pydub.playback import play
import pytube  
from pytube import YouTube

AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"

try:
    video_url = 'https://www.youtube.com/watch?v=UUheH1seQuE'

    vidid = pytube.YouTube(video_url).video_id

    audio_out = "finalout.wav"

    mylist = YouTubeTranscriptApi.get_transcript(vidid)

    length = len(mylist)

    startpoint = mylist[0]['start']

    startsegment = AudioSegment.silent(duration=startpoint*1000)

    audio_out = startsegment

    language = 'pt'
    for i in range(length):
        txt = (mylist[i]['text'])
        due = (mylist[i]['duration'])
        myText = txt
        filename = '.\\ttsout.wav'
        tts = gTTS(text = myText, lang = language, tld = 'com.br', slow = False)
        tts.save('ttsout.wav')
        aud1 = AudioSegment.from_file(filename)
        aud2 = AudioSegment.silent(duration=(due)*1000)
        output = aud2.overlay(aud1)
        audio_out = audio_out + output
        print(str(int((i/length)*100)) + "%") 
    audio_out.export("finalout.mp3")
    print("done")

except Exception as e:
    print(e)