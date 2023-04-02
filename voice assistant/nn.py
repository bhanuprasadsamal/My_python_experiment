import pyttsx3
import speech_recognition as sr
assistant =pyttsx3.init()
voices = assistant.getProperty('voices')
print(voices)
assistant.setProperty('voices',voices[0].id)

def speak(audio):
    assistant.say(audio)
    print(" ")
    assistant.runAndWait()


def takecommand():
  command = sr.Recognizer()
  with sr.Microphone() as source:
    print("listing....")
    command.pause_threshold = 1
    audio = command.listen(source)

    try:
        print("recogning...")
        query = command.recognize_google(audio,language='en-in')
        print(f"you said : {query}")

    except Exception as Error:
            return None
            return query
            


query = takecommand()
if 'hello' in query:
    speak("hello sir")

else:
    speak("no command found")