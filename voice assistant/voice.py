#                                   MAKING VOICE ASSISTANT USING PYTHON
#First install pyttsx3 (pip install pyttsx3)

import pyttsx3 as p
import speech_recognition as sr


""" to convert speech to text
1.install speechrecognition in terminall
pip install SpeechRecognition
2.install pyaudio 
 pip install pyAudio


"""
engine = p.init()
# rate is use to chake the voice speed
rate = engine.getProperty('rate')
print(rate)
"""
you can change the voice speed as bellow

rate=engine.getProperty('rate')
engine.setProperty('rate',180)
"""
"""   chake how many voice is you have
voice = engine.getProperty('voice')
print(voice)

we can change the voice by using the bellow code 

voice= engine.setProperty('voice',voice[0].id)
#chake another voice as use
voice[1] using in avobe
"""
engine.say("hello . I am your voice assistant ")
engine.runAndWait()

r =sr.Recognizer()
with sr.Microphone() as source:
    r.energy_threshold =10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
audio = r.listen(source)
text = r.recognize_google(audio)
print(text)
