import pyttsx3
import speech_recognition as sr
import pyaudio
import webbrowser
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
     if 'open google' in c.lower():
          webbrowser.open("www.google.com")
     elif 'open youtube' in c.lower():
          webbrowser.open("www.youtube.com")

if __name__ == '__main__':
    # print(sr.Microphone.list_microphone_names())
    speak("Initializing Marshmello")
    r = sr.Recognizer()
    while True:
        
            print("Recognizing....")
            try :
                with sr.Microphone() as source:
                    print("Listening....")
                    audio = r.listen(source)
                    word =  r.recognize_google(audio)
                    # print(word)
                if word.lower =='pakya':
                    speak("Jarvis Activated")
                    with sr.Microphone() as source:
                        print("Listening....")
                        audio = r.listen(source)
                        command =  r.recognize_google(audio)

                        processCommand(command)
            except Exception as e:
                print(e)