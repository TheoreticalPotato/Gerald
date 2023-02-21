'''Speech Engine'''
import pyttsx3

# TTS setup
engine = pyttsx3.init('sapi5')                    
engine.setProperty('rate', 230)     
engine.setProperty('volume', 1.0)    
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[0].id)

# Speaks the given input
def speak(audio):
    engine.say(audio)
    engine.runAndWait()