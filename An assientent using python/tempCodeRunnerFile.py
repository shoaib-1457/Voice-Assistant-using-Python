import pyttsx3  # Install module using pip
import datetime  #


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)


def speak(audio):  # Speak Funtion
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour <= 12 and hour < 17:
        speak("Good Afternoon")
    elif hour <= 17 and hour < 21:
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("I am kiki , Please tell me how may I help You")


if __name__ == "__main__":
    wishMe()
