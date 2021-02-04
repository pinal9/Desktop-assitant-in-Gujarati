import speech_recognition as sr
from googletrans import Translator
import datetime
from textblob import TextBlob
import pyttsx3
import os
import time
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    music_dir = 'C:\\Users\\Jitendra\\Desktop\\m1'
    songs = os.listdir(music_dir)
    trans = Translator()

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print('Good Morning')
        word = TextBlob('good Morning')
        w1 = word.translate(from_lang='en', to='gu-In')
        print(w1)
        speak("goodmorning")
        os.startfile(os.path.join(music_dir, songs[2]))


    elif hour>=12 and hour<18:
        print('Good Afternoon')
        word = TextBlob('good afternoon')
        w1 = word.translate(from_lang='en', to='gu-In')
        print(w1)
        speak("Good Afternoon!")
        os.startfile(os.path.join(music_dir, songs[0]))


    else:
        print('Good Evening')
        word = TextBlob('good evening')
        w1 = word.translate(from_lang='en', to='gu-In')
        print(w1)
        speak("Good Evening!")
        os.startfile(os.path.join(music_dir, songs[1]))


    time.sleep(4)
    print('How Can i help you?')
    word = TextBlob('How Can I Help You')
    w1 = word.translate(from_lang='en', to='gu-In')
    print(w1)
    speak("How  Can I help U ?")
    os.startfile(os.path.join(music_dir, songs[4]))
    time.sleep(4)


def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say Something:')
        print('listening....')
        audio = r.listen(source)


        try:
            text = r.recognize_google(audio,language='gu-IN')
            print (f"User Said:{text}")
            word = TextBlob(text)
            query = word.translate(from_lang='gu-IN',to='en')
            print(f"User Said:{query}")
            print('Done!')


        except:
            print('sorry something went wrong')
            print('Try Again!')
            return "None"

    return query


if __name__ == '__main__':
       wishMe()
       while True:
          query = takecommand().lower()

          if 'wikipedia' in query:
              speak('Searching Wikipedia...')
              query = query.replace("wikipedia","")
              print(query)
              results = wikipedia.summary(query, sentences=2)
              speak("According to Wikipedia")
              print(results)
              speak(results)

          elif 'open youtube' in query:
              webbrowser.open("youtube.com")

          elif 'open google' in query:
              webbrowser.open("google.com")

          elif 'time' in query:

              strTime = datetime.datetime.now().strftime("%H:%M:%S")
              trans = Translator()
              x = trans.translate(strTime,dest='gu')
              print(x.text)
              print("date and Time",strTime)
              speak(f"Sir, the time is {strTime}")


          






