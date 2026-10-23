import pyttsx3
import speech_recognition
import os
import datetime
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


extractedtime = open('Alarmtext.txt','rt')
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open('Alarmtext.txt','r+')
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace('set alarm','')
    timenow = timeset.replace(' and ', ':')
    timenow = timeset.replace(' ', ':')
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime('%H:%M:%S')
        if(currenttime == Alarmtime):
            speak('Alarm ringing, Sir')
            os.startfile('Alarm(Sound).mp3')
        elif(currenttime + '00:00:30' ==  Alarmtime):
            exit()

ring(time)