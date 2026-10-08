import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser

# Voice engine
engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)


# Speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# Recognizer
recognizer = sr.Recognizer()


# Main assistant loop
while True:

    try:
        with sr.Microphone() as source:
            print("\nListening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5)

        command = recognizer.recognize_google(audio).lower()

        print("You said:", command)

        # Tell time
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        # Open Notepad
        elif "notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        # Open Calculator
        elif "calculator" in command:
            speak("Opening Calculator")
            os.system("calc")

        # Open YouTube
        elif "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        # Open Google
        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        # Search Google
        elif "search" in command:
            search_query = command.replace("search", "").strip()

            if search_query:
                speak("Searching for " + search_query)
                webbrowser.open(
                    "https://www.google.com/search?q=" + search_query
                )
            else:
                speak("What should I search for?")

        # Exit
        elif "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye Sarthak!")
            break

        # Unknown command
        else:
            speak("Sorry, I don't know that command yet.")

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")

    except sr.WaitTimeoutError:
        print("No voice detected. Listening again...")

    except sr.RequestError:
        speak("There is a problem with the speech service.")

    except Exception as e:
        print("Error:", e)