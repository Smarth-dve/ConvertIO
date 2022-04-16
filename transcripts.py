from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
from googletrans import Translator
from pydub import AudioSegment
import pydub
from pydub.playback import play
import pytube  
from pytube import YouTube
import winsound

AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"

def combine_audio(vidname, audname, outname): 
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname)

try:
    # video_url = input("Enter url:")
    # language = input("Select language:")
    # accent = input("Select accent:")

    video_url = 'https://www.youtube.com/watch?v=UUheH1seQuE'
    language = 'fr'
    accent = 'fr'

    vidid = pytube.YouTube(video_url).video_id

    audio_out = "finalout.wav"

    mylist = YouTubeTranscriptApi.get_transcript(vidid)

    length = len(mylist)

    startpoint = mylist[0]['start']

    startsegment = AudioSegment.silent(duration=startpoint*1000)

    audio_out = startsegment


    translater = Translator()

    for i in range(length):
        txt = (mylist[i]['text'])
        due = (mylist[i]['duration'])
        out = translater.translate(txt, language)
        myText = out.text
        filename = 'D:\\Samarth\\Charusat\\Collage material\\Sem 4\\SGP\\ttsout.wav'
        tts = gTTS(text = myText, lang = language, tld=accent, slow = False)
        tts.save('ttsout.wav')
        aud1 = AudioSegment.from_file(filename)
        aud2 = AudioSegment.silent(duration=(due)*1000)
        output = aud2.overlay(aud1)
        audio_out = audio_out + output
        print(str(int((i/length)*100)) + "%") 
    audio_out.export("finalout.mp3")
    print("Audio Translated Successfully!")
    winsound.Beep(650, 500)

    youtube = pytube.YouTube(video_url)  
    video = YouTube(video_url).streams.get_highest_resolution().download(filename="outvideo.mp4")
    print("Video Downloaded Successfully!")

    combine_audio("outvideo.mp4", "finalout.mp3", "translatedvideo.mp4")

except Exception as e:
    print(e)
    myText = '''Sorry We didn't get that'''
    language = 'en'
    output = gTTS(text = myText, lang = language, tld="ca",slow = False)
    output.save("translatedvideo.mp3")
    winsound.Beep(440, 500)
