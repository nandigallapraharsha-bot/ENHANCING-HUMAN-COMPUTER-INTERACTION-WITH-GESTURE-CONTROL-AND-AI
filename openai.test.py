import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random

def ai(prompt):
    try:
        openai.api_key = "XXX"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt
        )

        return response.choices[0].message["content"]
    except Exception as e:
        print("Error:", str(e))
        return "Sorry, I couldn't process that."

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takecommand():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
        print("Error:", str(e))
        return ""

if __name__ == '__main__':
    print('pycharm')
    say("Hello, I am Jarvis A.I.")
    while True:
        print("Listening...")
        query = takecommand()

        # Using artificial intelligence
        if "using artificial intelligence" in query.lower():
            response = ai([
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ])
            print(response)
            say(response)

        # Sites to open
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir... ")
                webbrowser.open(site[1])

        # Open music
        if "open music" in query:
            musicpath = "C:\\Users\\hp\\Downloads\\Ripple - On Your Mind [NCS Release].mp3"
            os.startfile(musicpath)

        # Get the current time
        if "the time" in query:
            time_now = datetime.datetime.now().strftime("%H:%M")
            say(f"Sir, the time is {time_now}")

        # Open Chrome
        if "open chrome" in query.lower():
            os.system('start "" "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')

        if "open mouse pad" in query.lower():
            os.system('python "C:\\Users\\hp\\PycharmProjects\\voice assistant\\mouse pad.py"')

        if "open board" in query.lower():
            try:
                os.system(r'python "C:\Users\hp\PycharmProjects\voice assistant\keys.py"')
            except Exception as e:
                print("Error opening board:", str(e))

        if "open spotify" in query.lower():
            os.system("C:\\Users\\hp\\anaconda3\\pkgs\\protego-0.1.16-py_0\\info\\test\\tests\\test_data\\www.spotify.com")
