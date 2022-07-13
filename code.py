
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time
import wikipedia



def speech_to_txt():
    recongizer= sr.Recognizer()
    with sr.Microphone() as source:
        print("Now Listening.....")
        recongizer.adjust_for_ambient_noise(source) #to remove noise
        audio=recongizer.listen(source)
        try:
            print("Decoding....") 
            data=recongizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Able to Understand....   Sorry!!!")
#Speech to text part is completed above.
# text to Speech  part is completed below.
def text_to_speech(x):#speechtxt
    engine= pyttsx3.init()
    voices= engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)#0 for male and 1 for female voise
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)#speech rate canbe adjusted
    engine.say(x)
    engine.runAndWait()

if __name__=='__main__': #to split the program.
   

    while True:

        data1=speech_to_txt().lower()
        if "your name" in data1:
            name="my name is fibre"
            text_to_speech(name)
        elif "old are you" in data1:
            age="i am two years old"
            text_to_speech(age)
        elif "time" in data1:
            time=datetime.datetime.now().strftime("%I%M%p")
            text_to_speech(time)
        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
        elif "joke" in data1:
            joke_1=pyjokes.get_joke(language="en",category="neutral")
            text_to_speech(joke_1)
        elif "job" in data1:
            webbrowser.open("https://www.sarkariresult.com/")
        elif "sports" in data1:
            webbrowser.open("https://indianexpress.com/section/sports/")
        elif "exit" in data1:
            text_to_speech("thanks, have a good day")
            break
        elif "news" in data1:
            webbrowser.open("https://www.ndtv.com/")
        time.sleep(5)
    #else:
        #print("thanks")






