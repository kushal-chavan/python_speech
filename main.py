import speech_recognition as sr
import webbrowser
import time
import os
import random
import pyttsx3
from time import ctime

r = sr.Recognizer()

speaker = pyttsx3.init('sapi5')
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 173)


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            say(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            say('Sorry, I did not get that')
        except sr.RequestError:
            say('Sorry, my speech service is down')
        return voice_data


def say(audio_string):
    print('Computer: ' + audio_string)
    speaker.say(audio_string)
    speaker.runAndWait()


def respond(voice_data):
    if 'what is your name' in voice_data:
        say('My name is Kushal')
    if 'what time is it' in voice_data:
        say(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        say('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        say('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
say('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
