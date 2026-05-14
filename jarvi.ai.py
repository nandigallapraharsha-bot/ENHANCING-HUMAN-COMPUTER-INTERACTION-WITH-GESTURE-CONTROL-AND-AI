import pyttsx3 as p
import speech_recognition as sr
import datetime
import subprocess
import openai
from selenium_web import *
from YT_auto import *
import randfacts
from jokes import *
from weather import*
from News import *

# Initialize the OpenAI API key
openai.api_key = ""

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        return "good morning"
    elif 12 <= hour < 16:
        return "good afternoon"
    else:
        return "good evening"

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said:", text)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return ""
        except sr.RequestError as e:
            print("Request error from Google Speech Recognition service; {0}".format(e))
            return ""

def execute_python_file(file_path):
    try:
        return subprocess.Popen(["python", file_path])
    except FileNotFoundError:
        speak("Sorry, I couldn't find the file.")

def close_python_process(process):
    if process is not None:
        process.terminate()  # Terminate the Python process

def main():
    speak("Hello sir, " + wishme() + ", I'm your Jarvis.")
    today_date = datetime.datetime.now()
    speak("Today is " + today_date.strftime("%d") + " of " + today_date.strftime(" %B ") +
          " and it's currently " + today_date.strftime("%I:%M %p"))

    speak("The temperature in New Delhi is " + str(temp()) + " degree Celsius with " + str(des()))
    speak("What can I do for you?")

    while True:
        text = get_audio()

        if "what about you" in text:
            speak("I am also having a good day, sir")

        elif "information" in text:
            speak("You need information related to which topic?")
            infor = get_audio()
            speak("searching {} in Wikipedia".format(infor))
            assist = infow()
            assist.get_info(infor)

        elif "play video" in text:
            speak("You want me to play which video?")
            vid = get_audio()
            print("Playing {} on YouTube".format(vid))
            speak("Playing {} on YouTube".format(vid))
            assist = music()
            assist.play(vid)

        elif "news" in text:
            print("Sure sir, now I will read news for you")
            speak("Sure sir, now I will read news for you")
            arr = news()
            for news_item in arr:
                print(news_item)
                speak(news_item)

        elif "fact" in text:
            speak("Sure, sir, ")
            x = randfacts.getFact()
            print(x)
            speak("Did you know that, " + x)

        elif "joke" in text:
            speak("Sure sir, get ready for some chuckles")
            joke_list = joke()
            for joke_item in joke_list:
                print(joke_item)
                speak(joke_item)

        elif "write" in text or "say" in text:
            speak("What would you like me to write?")
            text_to_write = get_audio()
            print("You said:", text_to_write)
            with open("letter.txt", "w") as file:
                file.write(text_to_write)
            speak("I have written the content to the letter.txt file.")

        elif "open mouse pad" in text:
            subprocess.Popen(["python", "C:\\Users\\hp\\PycharmProjects\\voice assistant\\mouse pad.py"])

        elif "open keyboard" in text:
            subprocess.Popen(["python", "C:\\Users\\hp\\PycharmProjects\\voice assistant\\keyboard.py"])

        elif "exit" in text or "bye" in text:
            speak("Goodbye sir!")
            break

        else:
            speak("I'm sorry, I didn't catch that. Can you repeat?")

if __name__ == "__main__":
    main()
