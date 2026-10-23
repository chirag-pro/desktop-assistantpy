import json
import os

import pyttsx3
import requests
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


def LatestNews():
    """Read top business headlines for India using the NewsAPI service."""
    api_key = os.getenv("NEWSAPI_KEY")
    if not api_key:
        message = "News is not configured. Add NEWSAPI_KEY to your .env file."
        print(message)
        Speak(message)
        return

    url = "https://newsapi.org/v2/top-headlines"
    params = {"country": "in", "category": "business", "apiKey": api_key}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        payload = response.json()
    except (requests.RequestException, json.JSONDecodeError) as exc:
        print(f"Could not fetch news: {exc}")
        Speak("Sorry, I could not fetch the news right now.")
        return

    if payload.get("status") != "ok":
        message = payload.get("message", "The news service returned an error.")
        print(f"News API error: {message}")
        Speak("The news service returned an error.")
        return

    articles = payload.get("articles", [])
    if not articles:
        Speak("No business headlines were returned.")
        return

    Speak("Here are the latest business headlines for India.")
    for article in articles:
        title = article.get("title") or "Untitled headline"
        article_url = article.get("url") or "No article link available"
        print(f"\n{title}\nRead more: {article_url}")
        Speak(title)
        choice = input("Press 1 to continue to the next headline, or 0 to stop: ").strip()
        if choice != "1":
            break

    Speak("That is all for the news.")
