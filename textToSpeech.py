from gtts import gTTS
import os

myText = "Hello all"

language = 'en'

output = gTTS(text = myText, lang = language, tld="ca",slow = False)

output.save("TTSOutput.mp3")

os.system("start TTSOutput.mp3")