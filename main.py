import pyttsx3
import speech_recognition as sr
import pyaudio
import webbrowser
import requests



engine = pyttsx3.init()
r = sr.Recognizer()
newsapi = '********************************'

#this function will speak your text to speach
def speak(text):
    engine.say(text)
    engine.runAndWait()

#this function will process your commands
def processCommand(c):
    if 'open google' in c.lower():
        webbrowser.open("www.google.com")
    elif 'open youtube' in c.lower():
        webbrowser.open("www.youtube.com")
    elif 'open linkedin' in c.lower():
        webbrowser.open("www.linkedin.com")
    elif 'open github' in c.lower():
        webbrowser.open("www.github.com")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        data = r.json()
        for i, article in enumerate(data["articles"]):
            title = article["title"]
            speak(f"News {i+1}: {title}")
    elif 'exit' in c.lower():
            exit()
    elif 'restart' in c.lower():
        starts()
            

# this is main function
if __name__ == '__main__':
    # print(sr.Microphone.list_microphone_names())
    
    def starts():
        print("Initializing Jarvis")
        speak("Initializing Jarvis")
        while True:
            
                print("Recognizing....")
                try :
                    with sr.Microphone() as source:
                        print("Listening....")
                        audio = r.listen(source)
                        word =  r.recognize_google(audio)
                        # print(word)
                        
                    if word.lower() =='jarvis':
                        print("Jarvis Activated")
                        speak("Jarvis Activated")
                        # command_mode = True

                        while True:
                            with sr.Microphone() as source:
                                print("Listening for command....")
                                r.adjust_for_ambient_noise(source)
                                audio = r.listen(source, timeout=2, phrase_time_limit=10)
                                command =  r.recognize_google(audio)
                                print("Your Command is : ",command)
                                processCommand(command)
                except Exception as e:
                    print(e)
    starts() # calling starts function