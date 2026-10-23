# Desktop Assistant (Hey Buddy)

A Windows desktop voice assistant built with Python. It listens for spoken commands, replies with text-to-speech, and can open websites/apps, search the web, play YouTube content, control some media keys, read business headlines, tell the time, and save a short reminder in a text file.

> **Project status:** This is an older, rule-based desktop assistant, not a modern LLM chatbot. I reviewed the source and added setup documentation, a dependency file, environment-variable configuration for API keys, and a fix for the NewsAPI iteration/error handling. I have not been able to verify microphone, speaker, Windows app launching, or live API calls on your actual computer.

## Contents

```text
Desktop_assistant/
├── main.py                              # Main voice-assistant loop
├── alarm.py                             # Experimental alarm script; see limitations below
├── Alarm(Sound).mp3                     # Alarm audio
├── Alarmtext.txt                        # Temporary alarm time text file
├── Remember.txt                         # Saved reminder text
├── requirements.txt                     # Python dependencies
├── .env.example                         # Example API-key configuration
├── .gitignore                           # Excludes secrets and local files
└── Functions_file_for_Personal_assistance/
    ├── GreetMe.py                       # Greeting based on time of day
    ├── OpenApp.py                       # Opens/closes supported apps and websites
    ├── SearchNow.py                     # Google, YouTube, and Wikipedia searches
    ├── News.py                          # Business headlines for India
    ├── calculator.py                    # Wolfram|Alpha-powered calculator
    └── keyboard.py                      # Volume-key helpers
```

## Requirements

- Windows 10 or Windows 11. The project explicitly uses the Windows `sapi5` speech engine and Windows process-launching features.
- Python **3.11 or 3.12 recommended** for compatibility with the project's older audio/desktop dependencies. Python 3.14 has not been validated with this project.
- A working microphone and speakers/headphones.
- Internet access for online speech recognition and online search/news features.
- Optional API keys for business news and calculator features.

The microphone capture uses `SpeechRecognition` with its microphone support (`PyAudio`). The text-to-speech setup uses `pyttsx3` with the Windows SAPI5 driver.

## Installation (Windows PowerShell)

1. Extract the ZIP file. Open PowerShell or the VS Code terminal and move into the project folder—the folder containing `main.py`:

   ```powershell
   cd path\to\Desktop_assistant
   ```

2. Create a virtual environment. If Python 3.12 is installed:

   ```powershell
   py -3.12 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, you can skip activation and run the environment's Python directly as shown in the next commands, or use a permitted local execution-policy setting.

3. Upgrade pip and install the dependencies:

   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

   The `SpeechRecognition[audio]` requirement requests microphone/audio support. If installation reports a PyAudio error, install a compatible Python version and follow the current SpeechRecognition installation instructions linked in the References section.

4. Configure optional API keys. Create a local `.env` file from the example:

   ```powershell
   Copy-Item .env.example .env
   notepad .env
   ```

   Add your own key values:

   ```dotenv
   NEWSAPI_KEY=your_newsapi_key_here
   WOLFRAMALPHA_APP_ID=your_wolframalpha_app_id_here
   ```

   Keep `.env` private. It is excluded by `.gitignore`; do not put real keys in source code, screenshots, public repositories, or shared ZIPs. The app can start without these keys, but news or calculator requests will tell you when their configuration is missing.

## Run the assistant

From the project root, with the virtual environment active:

```powershell
python main.py
```

Keep the terminal open. When you see `Listening...`, speak clearly. The program uses Google's online speech-recognition service with the `en-in` language setting, so internet access is needed for voice recognition.

### Main voice commands

The assistant first waits for the wake phrase **“Hey Buddy”**. After the greeting, try commands such as:

| Say something like | What it does |
|---|---|
| `Hey Buddy` | Activates the command loop and greets you. |
| `What time is it` | Reads the current time. |
| `Open Chrome` / `Open VS Code` | Attempts to launch a supported Windows app. The app must be installed and its launch command available. |
| `Open example.com` | Opens a website if the spoken address is recognized by the simple URL check. |
| `Google search Python decorators` | Opens a web search and attempts to speak a short result. |
| `YouTube cats` | Opens/plays YouTube content related to the recognized query. |
| `Wikipedia machine learning` | Reads a short Wikipedia summary. |
| `What's the weather in Chandigarh` / `temperature in Chandigarh` | Attempts to read a result extracted from Google Search. This may break if the search-page layout changes. |
| `News` | Reads top business headlines for India; requires `NEWSAPI_KEY`. The terminal asks whether to continue to the next headline. |
| `Calculate 25 multiply 4` | Asks Wolfram|Alpha to evaluate an expression; requires `WOLFRAMALPHA_APP_ID`. |
| `Play some music` | Opens one of the hard-coded YouTube music links. |
| `Pause` / `Play` / `Mute` | Sends media-key presses to the currently active window. |
| `Volume up` / `Volume down` | Sends laptop-style function-key combinations; these depend on keyboard/hardware settings. |
| `Remember that buy groceries` | Saves the text after “remember that” to `Remember.txt`. |
| `What do you remember` | Reads the contents of `Remember.txt`. |
| `Wait Buddy` | Leaves the current command loop and returns to waiting for the wake phrase. |
| `Thanks Buddy` | Exits the assistant loop. |

Commands are matched with simple text conditions, not natural-language understanding. Use short, direct phrases. Some functions also read input from the terminal, so do not close the terminal while the assistant is running.

## API-key setup

- **News:** Create a key through [NewsAPI](https://newsapi.org/register) and place it in `NEWSAPI_KEY`. This implementation requests India's top business headlines.
- **Calculator:** Create an app ID through [Wolfram|Alpha Developer Portal](https://developer.wolframalpha.com/portal/myapps/) and place it in `WOLFRAMALPHA_APP_ID`.

The original project ZIP contained keys directly inside Python files. The prepared copy replaces those values with environment-variable lookups. **Please revoke or rotate the original keys** before using or publishing the project, because they were embedded in the shared source archive.

## Known limitations and items to improve

1. **Windows-only behavior:** `sapi5`, `os.startfile`, Windows `start`, and `taskkill` mean the project will not work as-is on macOS/Linux.
2. **Alarm is experimental/inactive:** The main file's alarm command block is commented out. The standalone `alarm.py` also has unreliable time-comparison logic. Do not rely on it for an important alarm until that code is rewritten and tested.
3. **Weather/temperature scraping:** These functions read HTML from Google Search and assume a particular element exists. Search-page changes, network errors, or rate limiting can make them fail.
4. **Search result quality:** Google/Wikipedia/YouTube routines are older implementations. Google search opens a browser, then separately attempts to fetch a Wikipedia summary; the spoken answer may not match the web results.
5. **Keyboard automation:** `pyautogui` sends keypresses to the active window. Focus the correct window before using playback, mute, volume, or close-tab commands.
6. **App launching varies by machine:** App names such as `code`, `chrome`, `winword`, and `excel` must be available through Windows' launch mechanism. You may need to edit the mapping in `OpenApp.py`.
7. **News/API availability:** NewsAPI limits and account permissions depend on the key/account. An API/network error will be printed to the terminal.
8. **Audio and recognition:** Windows microphone privacy permissions, the default recording device, internet connectivity, and the installed audio backend all affect speech recognition.
9. **Reminder storage:** `Remember.txt` holds only one reminder; each new “remember that” command replaces the previous text.

## Troubleshooting

### `ModuleNotFoundError: No module named ...`

Make sure the virtual environment is active and install the dependency list again:

```powershell
python -m pip install -r requirements.txt
```

### `AttributeError` or an error when creating `sr.Microphone()`

Microphone support may be missing. Confirm that `SpeechRecognition[audio]` installed successfully, check Windows microphone permissions, and verify that a microphone is available in Windows sound settings.

### Assistant does not hear commands

Check microphone permissions and the selected input device, reduce background noise, speak after `Listening...`, and verify internet access. This version uses online Google speech recognition; it is not offline speech recognition.

### Voice output does not work

Confirm that Windows audio output works and test the default output device. The code requests the Windows SAPI5 driver through `pyttsx3`.

### News or calculator says the key is missing

Check that a file named `.env` exists beside the project files, has the exact variable names `NEWSAPI_KEY` and `WOLFRAMALPHA_APP_ID`, and contains your own valid keys. Restart `python main.py` after changing `.env`.

### An app does not open or close

Edit the app-to-command mapping in `Functions_file_for_Personal_assistance/OpenApp.py`. The configured application command must match the software installed on the computer. Close-app commands can forcibly terminate a process, so use them cautiously.

### Run from VS Code

Open the **Desktop_assistant** folder itself in VS Code, select the virtual environment's Python interpreter, open a terminal in that folder, then run:

```powershell
python main.py
```

Do not run a helper file as the main program unless you are testing that module specifically.

## Security and privacy notes

- Do not commit `.env`; use `.env.example` for placeholders only.
- Voice recognition uses an online service, so spoken audio is sent for recognition by the service used by `recognize_google`.
- App/keyboard commands have real effects on the computer. Review the command before running it and keep focus on the intended window.
- Avoid running the project with administrator privileges unless a specific, understood requirement makes it necessary.

## References

- [SpeechRecognition on PyPI — installation and microphone requirements](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3 on PyPI](https://pypi.org/project/pyttsx3/)
- [python-dotenv documentation on PyPI](https://pypi.org/project/python-dotenv/)
- [NewsAPI](https://newsapi.org/)
- [Wolfram|Alpha Developer Portal](https://developer.wolframalpha.com/portal/myapps/)
