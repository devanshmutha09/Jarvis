import speech_recognition as sr

print("Mic access test starting...")

try:
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening for 2 seconds...")
        audio = r.listen(source, timeout=2, phrase_time_limit=2)
        print("Captured audio.")
except Exception as e:
    print("Error accessing microphone:", e)