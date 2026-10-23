import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
import time

# Initialize the speech engine
engine = pyttsx3.init('sapi5')

# Set voice and speaking rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def Speak(audio):
    """Function to make the assistant speak."""
    engine.say(audio)
    engine.runAndWait()

def GetCommand():
    """Function to get the user's spoken command."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300
        audio = recognizer.listen(source, 0, 4)

        try:
            print('Recognizing...')
            query = recognizer.recognize_google(audio, language='en-in')
            print(f'You said: {query}\n')
            return query
        except Exception as e:
            print("Please repeat yourself, I can't recognize that.\n")
            return 'None'


def alarm(query):
    timehere = open('Alarmtext.txt','a')
    timehere.write(query)
    timehere.close()
    os.startfile('alarm.py')

if __name__ == '__main__':

    Start = True
    while Start:
        query = GetCommand().lower()
        print(f"Recognized command: {query}")  # Debugging print

        if 'hey buddy' in query:
            from Functions_file_for_Personal_assistance.GreetMe import greetMe
            greetMe()

            while True:
                query = GetCommand().lower()
                print(f"Recognized command inside loop: {query}")  # Debugging print

                if 'thanks buddy' in query:
                    Speak('Ok Boss, you can call me anytime.')
                    Start = False
                    break
                
                elif 'wait buddy' in query:
                    Speak('Ok Boss, I am waiting')
                    break

                elif 'hello' in query:
                    Speak('Hello sir, how are you?')
                
                elif 'i am fine' in query:
                    Speak('I am glad you are fine')
                
                elif 'how are you' in query:
                    Speak('Perfect sir')
                
                elif 'thank you' in query:
                    Speak('You are welcome Boss')
                
                elif 'open' in query:
                    from Functions_file_for_Personal_assistance.OpenApp import openAppweb
                    openAppweb(query)
                
                elif 'close' in query:
                    from Functions_file_for_Personal_assistance.OpenApp import closeAppweb
                    closeAppweb(query)
            
                elif 'google' in query:
                    from Functions_file_for_Personal_assistance.SearchNow import SearchGoogle
                    SearchGoogle(query)
                elif 'youtube' in query:
                    from Functions_file_for_Personal_assistance.SearchNow import SearchYoutube
                    SearchYoutube(query)

                elif 'wikipedia' in query:
                    from Functions_file_for_Personal_assistance.SearchNow import SearchWikipedia
                    SearchWikipedia(query)

                elif 'pause' in query:
                    pyautogui.press('k')
                    Speak('you pause it')

                elif 'play' in query:
                    pyautogui.press('k')
                    Speak('You played it')

                elif 'mute' in query:
                    pyautogui.press('m')
                    Speak('You muted it')

                elif 'volume up' in query:
                    from Functions_file_for_Personal_assistance.keyboard import volumeup
                    Speak('Turning the volume up, Boss')
                    volumeup()
                
                elif 'volume down' in query:
                    from Functions_file_for_Personal_assistance.keyboard import volumedown
                    Speak('Turning the volume down, Boss')
                    volumedown()

                elif 'play some music' in query:
                    Speak('Playing some song, Boss')
                    a = (1,2,3)
                    randSong = random.choice(a)

                    if randSong==1:
                        webbrowser.open('https://youtu.be/jJvDnYdD8JQ?si=7oy-Q4aCWTi0fQ68')
                        time.sleep(2)
                        pyautogui.press('k')
                        time.sleep(1)
                        pyautogui.hotkey('Alt','Tab')

                    elif randSong==2:
                        webbrowser.open('https://youtu.be/cKs83ZQxYKA?si=HfxTu9d6jJcejX47')
                        time.sleep(2)
                        pyautogui.press('k')
                        time.sleep(1)
                        pyautogui.hotkey('Alt','Tab')
                    else:
                        webbrowser.open('https://youtu.be/I2uPSqNqrqU?si=DhyfoLY4Q3ymVKDU')
                        time.sleep(2)
                        pyautogui.press('k')
                        time.sleep(1)
                        pyautogui.hotkey('Alt','Tab')

                elif 'temperature' in query:
                    # query = query.replace('te')
                    search = f'{query}'
                    url = f'https://www.google.com/search?q={search}'
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,'html.parser')
                    temp = data.find('div', class_ = 'BNeawe').text  
                    Speak(f'Current{search} is {temp}')

                elif 'news' in query:
                    from Functions_file_for_Personal_assistance.News import LatestNews
                    LatestNews()

                elif 'calculate' in query:
                    from Functions_file_for_Personal_assistance.calculator import Wolframalpha
                    from Functions_file_for_Personal_assistance.calculator import calc
                    query = query.replace('calculate','')
                    calc(query)


                elif 'weather' in query:
                    search = f'{query}'
                    url = 'https://www.google.com/search?q={search}'
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,'html.parser') 
                    weather = data.find('div', class_ = 'BNeawe').text
                    Speak(f'The curent {search} is {weather}')

                elif 'time' in query:
                    strtime = datetime.datetime.now().strftime('%H:%M:%S')
                    Speak(f'Sir, The time is {strtime}')

                # elif 'set alarm' or 'alarm' in query:
                #     print('Input time example:- 10 and 10 and 10')
                #     Speak(f'Set the alarm')
                #     time = input('Enter the time (hr and min and sec)')
                #     alarm(time)
                #     Speak('Done, Boss')

                elif 'remember that' in query:
                    RememberMessage = query.replace('remember that','')
                    Speak('You told me remember that : ' + RememberMessage)
                    remember = open('Remember.txt','w')
                    remember.write(RememberMessage)
                    remember.close()

                elif 'what do you remember' in query:
                    remember = open('Remember.txt')
                    Speak('You told me to remember that to '+ remember.read())

                else:
                    if query == 'none':
                        pass
                    else:
                        query = query + ' google'
                        from Functions_file_for_Personal_assistance.SearchNow import SearchGoogle
                        SearchGoogle(query)


