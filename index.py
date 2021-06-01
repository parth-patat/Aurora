# welcome msg
    #greet, date and time
# google search
# chrome search
# Shutdown, logout and restart
# Playing songs
# remembering to do list
# taking screen shot
# CPU, battery stats
# Jokes
# 1-2 games
# Coming soon.....

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
                      
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        return "None"
    return query

speak("This is Jarvis")

def time():
    currentTime = datetime.datetime.now().strftime("%I:%M")
    speak("time is")
    speak(currentTime)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)

    speak("date is")
    speak(day)

def greet():
    speak("Welcome back sir!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good morning!")
    elif hour >=12 and hour <17:
        speak("Good afternoon!")
    elif hour >=17 and hour <24:
        speak("Good evening!")
    
    speak("What can I do for you sir?")

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("sender's mail", "password")
    server.sendmail("sender's mail", to, content)
    server.close()

if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'day' or 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summery(query, sentences=2)
            print(result)
            speak(result)
        elif "send mail" in query:
            try:
                speak("On it sir, what should I say?")
                content = takeCommand()
                speak("who's the reciever?")
                to = takeCommand()
                sendEmail(to, content)
                speak("Sir, It's done")
            except Exception as e:
                print(e)
                speak("Sorry sir, Email system is compromized")
        elif 'offline' in query:
            speak("Alright sir, see you soon")
            quit()