from email.mime import audio
from imp import source_from_cache
from operator import ipow
import pyaudio
from winreg import QueryInfoKey

import pyttsx3  # Install module using pip by pip install pyttsx3
import speech_recognition as sr  # Install using pip by pip install speechRecognition
import datetime  # Inbuilt module in the Python
import wikipedia # pip install wikipedia
import webbrowser # built in module
import os
import smtplib  # built in module


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()




def speak(audio):  # Speak Funtion
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour <= 12 and hour < 17:  # when we will run the code the bot will greet us
        speak("Good Afternoon")
    elif hour <= 17 and hour < 21:
        speak("Good Evening")
    else:
        speak("Good Evening")

    speak("I am kiki , Please tell me how may I help You")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "play music" in query:
            webbrowser.open("gaana.com")
        elif "open amazon" in query:
            webbrowser.open("amazon.com")
        elif "open insta" in query:
            webbrowser.open("instagra.com")
        elif "email to anshu" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sheikhshoaib1457@gmail.com"
                speak("Email has sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send the email")
