import speech_recognition as sr

print("Checking mic...")
with sr.Microphone() as source:
    print("Mic opened!")