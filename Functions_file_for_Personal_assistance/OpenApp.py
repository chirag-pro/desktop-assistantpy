import os
import pyautogui
import webbrowser
import pyttsx3
import speech_recognition
import time 

engine = pyttsx3.init('sapi5')

# Set voice and speaking rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def Speak(audio):
    """Function to make the assistant speak."""
    engine.say(audio)
    engine.runAndWait()

dictApp = {
    'command prompt': 'cmd',
    'paint': 'mspaint',
    'excel': 'excel',
    'word': 'winword',
    'vs code': 'code',
    'chrome': 'chrome',
    'powerpoint': 'powerpnt',
    'whatsapp' : 'whatsapp',
    'youtube': 'youtube'
    
}

def openAppweb(query):
    Speak('Launching, Sir')
    query = query.lower().replace('open', '').replace('launching', '').strip()
    
    if any(ext in query for ext in ['.com', '.in', '.org']):
        query = query.replace('dot', '.').replace(' ', '')
        webbrowser.open(f'https://{query}')
    else:
        found = False
        for app in dictApp.keys():
            if app in query:
                os.system(f'start {dictApp[app]}')
                found = True
                break
        if not found:
            Speak("Sorry sir, app doesn't present")

def closeAppweb(query):
    Speak('Closing, Sir')
    if 'tab' in query:
        time.sleep(0.5)  # Wait to ensure Chrome is active
        pyautogui.hotkey('ctrl', 'w')  # Close the tab
        Speak('tab is closed')
    else:
        found = False
        for app in dictApp.keys():
            if app in query:
                os.system(f'taskkill /f /im {dictApp[app]}.exe')
                found = True
                break
        if not found:
            Speak("Sorry sir, app doesn't present")
