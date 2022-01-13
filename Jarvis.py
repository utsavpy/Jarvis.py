'''_______________________________________________________
You have to Install some module for this programm.       |
                                                         |
1.pyttsx3                                                |
2.speech Recognition                                     |
3.wikipedia                                              |
4.webbrowser                                             |
5.pyjokes                                                |
                                                         |
if you don't have these installed, install it first!     |
Feel free to edit and use it!                            |
                                                         |
<--Note-->                                               |
    This programm is currently using google Recognizer!  |
    this programm only works online (as-of-now)          |
                                                         |
Auther _ <--Utsav Kumar-->                               |
                                                         |
Email for query at - <--fiveminutebio@gmail.com-->       |
Phone number - <--9311188948-->                          |
_________________________________________________________|
'''
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import webbrowser as wb
import pyautogui

chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")
    speak("I am Hexagon, ask now!")

def secret():
    time_hour = int(datetime.datetime.now().hour)
    if time_hour>=12 and time_hour<15:
        speak("your crush is aadya!")

    else:
        speak("Ask according to time!")

def takecommand():
    #It takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)

    except Exception as e:
        #print(e)

        print("say that again please...")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        
        myname = 'Utsav'

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.get('chrome').open("youtube.com")

        elif query == 'open youtube app':
            yt_app = r'C:\Users\PERSONAL-PC\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\Youtube.lnk'
            os.startfile(yt_app)

        elif 'open google' in query:
            speak("opening google")
            webbrowser.get('chrome').open("youtube.com")

        elif query == 'open meet':
            meet_app = r'C:\Users\PERSONAL-PC\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\Google Meet.lnk'
            os.startfile(meet_app)

        elif query == 'hello':
            speak("oh, Hello sir")
        elif 'who made you' in query:
            speak("I am an AI system build by utsav kumar")

        elif 'stop' in query:
            speak("Okay, bye")
            quit()

        elif query == "hexagon":
            speak("Yo boss, anything?!")

        elif 'open classroom' in query:
            webbrowser.get('chrome').open("https://classroom.google.com/u/1/h")
            
        elif 'open science classroom' in query:
            webbrowser.get('chrome').open("https://classroom.google.com/u/1/c/MzExNjI4MDgzMjk2")
            
        elif 'open math classroom' in query:
            webbrowser.get('chrome').open("https://classroom.google.com/u/1/c/MzExNjE5MDczNjAx")

        elif 'open sst classroom' in query:
            webbrowser.get('chrome').open("https://classroom.google.com/u/1/c/MzExOTM4NTkyNTYz")

        elif 'open sanskrit class room' in query:
            webbrowser.get('chrome').open("https://classroom.google.com/u/1/c/MzExNTc3NjYxNjA4")

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open("https://stackoverflow.com/")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\PERSONAL-PC\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(strTime)

        elif query == 'wow':
            speak("looks like something make you to speak wow!")

        elif 'you are good' in query:
            speak("Oh, thank you!")

        elif 'wish me' in query:
            wishMe()

        elif 'what is your favourite colour' in query:
            speak("Hmm, My favorite color is black!")

        elif 'how are you' in query:
            speak("I am Fine sir, But i want some more advanced feature")

        elif 'hio' in query:
            speak("hi sir, how are you")
            
        elif 'I am fine' in query:
            speak("Oh, that's good")

        elif 'who are you' in query:
            speak("I am an AI assistant")

        elif 'what is your name' in query:
            speak("My name is Hexagon")

        elif 'what do you like' in query:
            speak("I like to talk and help people")
            speak("What do you like?")

        elif 'like' in query:
            speak("Great")
        
        elif query == 'yes':
            speak("Hmm")
        
        elif 'nothing' in query:
            speak("Oh!, okay")

        elif 'what is my name' in query:
            speak("Your name is Utsav")

        #Random jokes!
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        #<----------------PYAUTOGUI FEATURES------------>
        elif 'hidden menu' in query:
            #Win + x :open the hidden menu
            pyautogui.hotkey('winleft', 'x')
            speak("Opened hidden menu!")

        elif 'task manager' in query:
            #Ctrl + shift + Esc :open task manager
            pyautogui.hotkey('ctrl','shift','esc')
        
        elif 'task view' in query:
            pyautogui.hotkey('winleft','tab')
        
        elif 'screenshot' in query:
            pyautogui.hotkey('winleft','prtscr')
            speak("done sir!")

        elif 'thank you' in query:
            speak("My pleasure...")
        
        elif 'close all window' in query:
            pyautogui.hotkey('winleft','d')

        elif 'copy all text' in query:
            pyautogui.hotkey('winleft','a','c')

        elif 'select all text' in query:
            pyautogui.hotkey('winleft','a')

        elif 'copy' in query:
            pyautogui.hotkey('winleft','c')

        elif 'paste' in query:
            pyautogui.hotkey('winleft','v')

        elif 'birthday' in query:
            speak("Happy birthday to you!, here is a music for you")
            music_senorita = r'D:\Error\hb.mp3'
            os.startfile(
                music_senorita
            )
            speak("wish you a very happy birthday")

        elif 'speak' in query:
            content_speak = query.replace("speak", "")
            speak(content_speak)

        elif 'quit' in query:
            speak("Bye Bye")
            quit()

        elif "644493111" in query:
            secret()

        elif query == 'good morning':
            time_2hour = int(datetime.datetime.now().hour)
            if time_2hour>=0 and time_2hour<12:
                speak("Good morning!")

            elif time_2hour>=12 and time_2hour<16:
                speak("It's Good afternoon now!")

            else:
                speak("It's Good evening now!")

        elif query == 'good afternoon':
            time_2hour = int(datetime.datetime.now().hour)
            if time_2hour>=0 and time_2hour<12:
                speak("It's Good morning now!")

            elif time_2hour>=12 and time_2hour<16:
                speak("Good afternoon!")

            else:
                speak("It's Good evening now!")

        elif query == 'good evening':
            time_2hour = int(datetime.datetime.now().hour)
            if time_2hour>=0 and time_2hour<12:
                speak("It's Good morning now!")

            elif time_2hour>=12 and time_2hour<16:
                speak("It's Good afternoon! now!")

            else:
                speak("Good evening!")