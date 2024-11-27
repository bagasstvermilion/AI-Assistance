import speech_recognition as spc
from gtts import gTTS
import os
from playsound import playsound

def command():
    listening = spc.Recognizer()
    with spc.Microphone() as source:
        os.system('cls')
        print('Status : Mendengarkan....')
        voice = listening.listen(source,phrase_time_limit=10)
        try: 
            os.system('cls')
            print('Status : Diterima...')
            listen = listening.recognize_google(voice, language='id-ID')
            print(f"\nTranskrip : {listen}")
        except: 
            pass
        return listen

def speak(self):
    teks = (self)
    bahasa = 'id'
    namaFile = 'speak.mp3'
    def reading():
        voice = gTTS(text=teks, lang=bahasa, slow=False)
        voice.save(namaFile)
        playsound(namaFile)

    reading()

def runElysia():
    util = command()
    speak(util)

runElysia()