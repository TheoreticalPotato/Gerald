'''Take Voice Command'''
import speech_recognition as sr
import keyboard as kb
from popup import popup

# Takes command
def takeCommand():
    
    r = sr.Recognizer()
    # Uses default system microphone
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    # Tries to do recognize your voice
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    # If voice can't be recognized
    except Exception as e:
        print(e)   
        print("Unable to recognize your goofy ass voice") 
        return "None"
    # Replaces 'gerald' and 'hey' so it doesnt mess up the command
    if 'Gerald' or 'hey Gerald' in query:
        query = query.replace("Gerald", "")
        query = query.replace("hey", "")
        return query
    
    # Will not register if query does not incklude "Gerald"
    else:
        query = ""
        return query 