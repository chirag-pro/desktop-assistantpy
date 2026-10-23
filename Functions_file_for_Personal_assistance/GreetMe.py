import pyttsx3
import datetime
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hours = int(datetime.datetime.now().hour)

    if hours>=0 and hours<=12:
        speak('Good Morning Boss')
    
    elif hours>12 and hours<=18:
        speak('Good Afternoon Boss')
    
    elif hours>18 and hours<=20:
        speak('Good Evening Boss')

    else:
        speak('Good Night Boss')

    speak('How i can help you ?')


if __name__ == '__main__':
    greetMe()