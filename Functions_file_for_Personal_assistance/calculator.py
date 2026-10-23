import os

import pyttsx3
import speech_recognition  # Kept for compatibility with the original project.
import wolframalpha
from dotenv import load_dotenv

load_dotenv()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
if voices:
    engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)


def Speak(audio):
    """Speak a message using Windows text-to-speech."""
    engine.say(str(audio))
    engine.runAndWait()


def Wolframalpha(query):
    """Ask Wolfram|Alpha to evaluate a query using an environment-stored app ID."""
    app_id = os.getenv("WOLFRAMALPHA_APP_ID")
    if not app_id:
        print("Calculator is not configured. Add WOLFRAMALPHA_APP_ID to .env.")
        return None

    try:
        client = wolframalpha.Client(app_id)
        response = client.query(query)
        return next(response.results).text
    except Exception as exc:
        print(f"Could not calculate that query: {exc}")
        return None


def calc(query):
    term = str(query).lower()
    replacements = {
        "hey buddy": "",
        "multiply": "*",
        "into": "*",
        "plus": "+",
        "add": "+",
        "divide": "/",
        "minus": "-",
        "subtract": "-",
        "percentage": "%",
    }
    for word, symbol in replacements.items():
        term = term.replace(word, symbol)

    result = Wolframalpha(term.strip())
    if result is None:
        Speak("Sorry, I could not calculate that. Check the calculator API setup or query.")
        return

    print(result)
    Speak(result)
