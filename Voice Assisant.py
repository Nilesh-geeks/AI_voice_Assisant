import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nileshsln34@gmail.com', 'AlcoholPhenol')
    server.sendmail('nileshsln34@gmail.com', to, content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon")

    else :
        speak("Good Evening")

    speak("I am AI assistant . How can I help you ")


def takecommand():
    ''' It takes input from user and return string ouput'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print((sr.Microphone.list_microphone_names))
        print("Listening...")
        # r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        # print(e)
        print("Sorry, Didn't Recognized . Please say again...")
        return "None"
    return query



if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

        # logic for executing based on query
        if 'wikipedia' in query:
            speak('Searching the wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\HP\Music\music mobile'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {time}")
            speak(time)
        elif 'open pycharm' in query:
            codepath = "C:\\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains"
            speak("Opening the pycharm")
            os.startfile(codepath)
        elif 'open visual studio code' in query:
            codepath = "C:\\Users\HP\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
            speak("Opening the visual studio code")
            os.startfile(codepath)

        elif 'email' or 'a mail' in query:
            try:
                speak("what information you would like to send")
                content = takecommand()
                to = "nileshsln3@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                speak("Some Error Occurred . Please try again")


        elif (query in ['quit','exit','stop','bye','goodbye','see you again','exit the system']) or ('quit' in query):
            sys.exit()


    # speak("Nilesh has developed me : Hello , I am AI Assistant")