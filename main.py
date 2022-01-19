import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os


r = sr.Recognizer()

def startConvertion(path = 'AUD1.wav'):
    with sr.AudioFile(path) as source:
        print('Fetching File')
        audio_text = r.record(source, duration=14)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
        
            # using google speech recognition
            print('Converting audio transcripts into text ...')
            text = r.recognize_google(audio_text, language="hi-IN")
            # print(text)

            translater = Translator()
            out = translater.translate(text, dest = 'en')
            # print(out.text)
            myText = out.text
            language = 'en'
            output = gTTS(text = myText, lang = language, tld="ca",slow = False)

            output.save("TTSOutput.mp3")

            os.system("start TTSOutput.mp3")

        except :
            print('Sorry.. run again...')

startConvertion('MyRecording.wav')