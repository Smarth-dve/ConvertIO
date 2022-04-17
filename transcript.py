from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
from googletrans import Translator
from pydub import AudioSegment
import pydub
from pydub.playback import play
import pytube  
from pytube import YouTube

AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"
video_url = input()
try:
#    enter your URL Link here! 
    video_url = 'https://www.youtube.com/watch?v=UUheH1seQuE'

    vidid = pytube.YouTube(video_url).video_id

    audio_out = "finalout.wav"

    mylist = YouTubeTranscriptApi.get_transcript(vidid)

    length = len(mylist)

    startpoint = mylist[0]['start']

    startsegment = AudioSegment.silent(duration=startpoint*1000)

    audio_out = startsegment
    
    
    language = 'fr'
    accent = 'fr'

    translater = Translator()

    for i in range(length):
        txt = (mylist[i]['text'])
        due = (mylist[i]['duration'])
        myText = txt
        out = translater.translate(myText, dest = language)
        myText = out.text
        filename = 'D:\\SGP\\SGP SEM4\\Transcript\\ttsout.wav'
        tts = gTTS(text = myText, lang = language, tld=accent, slow = False)
        tts.save('ttsout.wav')
        aud1 = AudioSegment.from_file(filename)
        aud2 = AudioSegment.silent(duration=(due)*1000)
        output = aud2.overlay(aud1)
        audio_out = audio_out + output
        print(str(int((i/length)*100)) + "%") 
    audio_out.export("finalout.mp3")
    print("Audio Translated Successfully!")

except Exception as e:
    print(e)
    myText = '''Sorry We didn't get that'''
    language = 'en'
    output = gTTS(text = myText, lang = language, tld="ca",slow = False)
    output.save("translatedvideo.mp3")
