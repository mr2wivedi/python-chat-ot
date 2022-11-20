import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
from googlesearch import *
import pathlib
import random




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")

    speak("How may I help you?")



def takeCommand():
    #takes microphone input from the user and returns string output
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  
        r.pause_threshold = 1  
        r.energy_threshold=300
        audio=r.listen(source)
        

    try:
        print("Recognizing...") 
        query=r.recognize_google(audio, language='en-in')  
        print(f"User said: {query}\n")

    except Exception as e:

        print("Please say again...")
        return "None"
    return query
           

if __name__== "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        #logics for executing tasks based on queryp

        if 'open youtube' in query:
            webbrowser.open("youtube.com")
            break

        elif 'open google' in query:
            webbrowser.open("google.com")
            break

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            break

        elif 'open whatsapp' in query:
            whatsapp_path='C:\\Users\\dwish\\AppData\\Local\\WhatsApp\\Whatsapp.exe'
            os.startfile(whatsapp_path)
            break
        
        elif 'open notepad' in query:
            notepad_path='"C:\\Windows\\notepad.exe"'
            os.startfile(notepad_path)
            break
        elif 'open excel'in query:
            excel_path='"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"'
            os.startfile(excel_path)
            break

        elif 'open word'in query:
            excel_path='"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"'
            os.startfile(excel_path)
            break
            

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is:{strTime}")
            break

        

        elif 'play music' in query:
            music_dir = 'C:\\Users\\dwish\\Music'
            
            songs = os.listdir("C:\\Users\\dwish\\Music")
            print(songs)    
            os.startfile(os.path.join(music_dir, random.choice(songs)))
            #os.startfile(music_dir)
            break

        
        else :
            #speak("ask your question. i am listening...")
            #question=takeCommand().lower()

            chrome_path = '"C:\\Users\\Public\\Desktop\\Google Chrome"'
            for url in search(query, num_results=1):
                webbrowser.open("https://google.com/search?q=%s" % query)
            break



from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/myapp')
def voice():
        speak("Good Morning")
        while True:
            query=takeCommand().lower()

            #logics for executing tasks based on queryp

            if 'open youtube' in query:
                webbrowser.open("youtube.com")
                break

            elif 'open google' in query:
                webbrowser.open("google.com")
                break

            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")
                break

            elif 'open whatsapp' in query:
                whatsapp_path='C:\\Users\\dwish\\AppData\\Local\\WhatsApp\\Whatsapp.exe'
                os.startfile(whatsapp_path)
                break
            
            elif 'open notepad' in query:
                notepad_path='"C:\\Windows\\notepad.exe"'
                os.startfile(notepad_path)
                break
            elif 'open excel'in query:
                excel_path='"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"'
                os.startfile(excel_path)
                break

            elif 'open word'in query:
                excel_path='"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"'
                os.startfile(excel_path)
                break
                

            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is:{strTime}")
                break

            

            elif 'play music' in query:
                music_dir = 'C:\\Users\\dwish\\Music'
                
                songs = os.listdir("C:\\Users\\dwish\\Music")
                print(songs)    
                os.startfile(os.path.join(music_dir, random.choice(songs)))
                #os.startfile(music_dir)
                break

            
            else :
                #speak("ask your question. i am listening...")
                #question=takeCommand().lower()

                chrome_path = '"C:\\Users\\Public\\Desktop\\Google Chrome"'
                for url in search(query, num_results=1):
                    webbrowser.open("https://google.com/search?q=%s" % query)
                break
        return "null"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
