import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')

# Set voice and speaking rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
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
    return query


def SearchGoogle(query):
    if 'google' in query:
        import wikipedia as googleScrap
        query = query.replace('google search','')
        query = query.replace('google','')
        speak('This is what i found on google')

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak('No item found on search')


def SearchYoutube(query):
    if 'youtube' in query:
        import wikipedia as youtubeScap
        query = query.replace('youtube search','')
        query = query.replace('youtube','')
        web = 'https://www.youtube.com/results?search_query=' + query
        webbrowser.open(web)
        speak('this is i found on youtube')

    try:
        pywhatkit.playonyt(query)
        speak('Done Sir')

    except:
        speak('No item found on search')


def SearchWikipedia(query):
    if 'wikipedia' in query:
        speak('Searching from wikipedia....')
        query = query.replace('wikipedia','')
        query = query.replace('search wikipedia','')
        result = wikipedia.summary(query,sentences = 2)
        speak('According to wikipedia')
        print(result)
        speak(result)