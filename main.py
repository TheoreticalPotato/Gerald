#Importing of libraries and definition of key variables
import subprocess 
import wolframalpha # pip install wolframaplha
# WolframAlpha client key
client = wolframalpha.Client("API keys here")
import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speech_recognition
import datetime # pip install datetime
import wikipedia # pip install wikipedia
import webbrowser # pip install webbrowser
from AppOpener import run
import pyttsx3 # pip install pyttsx3

# TTS setup
engine = pyttsx3.init('sapi5')                    
engine.setProperty('rate', 230)     
engine.setProperty('volume', 1.0)    
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[0].id)
currentTime = datetime.datetime.now()

# Speaks the given input
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Greets user
def greeting():
    hour = int(datetime.datetime.now().hour)
    # Returns good morning if time is 12am - 12pm
    if hour >= 0 and hour<12:
        speak("Good Morning")
    # Returns good afternoon if time is 12pm - 18pm
    elif hour >= 12 and hour<18:
        speak("Good Afternoon")  
    # Returns good evening if time is 18pm - 12am
    else:
        speak("Good Evening") 

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

if __name__ == '__main__':
    greeting()
    speak("what can I do for you today")

    while True:
        query = takeCommand()
        # Wikipedia search
        if 'wikipedia' in query:  
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            wiki_ans = wikipedia.summary(query, sentences = 2)
            speak(wiki_ans)
        # Returns time
        elif 'time' in query:   
            speak("The time is now: %s:%s" % (currentTime.hour, currentTime.minute))
        # Terminates program
        elif 'exit' in query:
            speak("killing gerald")
            speak("what a world. what a world.")
            print("you have killed Gerald, you monster")
            exit()
        # Calculates math problem via WolframAlpha
        elif 'calculate' in query:  
            query = query.replace("calculate", "")
            res = client.query(query)                             
            wolfram_res = next(res.results).text
            speak(f"the answer to {query} is {wolfram_res}")
            print(wolfram_res)
        # Searches in browser
        elif 'search' in query:     
            query = query.replace("search", "")
            speak("searching on the web")
            webbrowser.open(query)
        # Opens Taiwan News in browser
        elif 'news' in query:       
            speak("opening taiwan news")
            webbrowser.open("taiwannews.com.tw")
        # Shuts down computer
        elif 'shutdown' in query:
            speak("shutting down your computer")
            subprocess.call('shutdown /s')
            exit()
        # Reboots computer
        elif "restart" in query:        
            subprocess.call(["shutdown", "/r"])
            exit()
        # Returns weather at current location via WolframAlpha
        elif "weather" in query:
            res = client.query(query)                             
            wolfram_res = next(res.results).text
            speak(f"the weather is currently {wolfram_res}")
            print(wolfram_res)
        # Returns definition of word via WolframAlpha
        elif "definition" in query:
            query = query.replace("define", "")
            res = client.query(query)                             
            wolfram_res = next(res.results).text
            speak(f"the definition of {query} is {wolfram_res}")
            print(wolfram_res)
        # Returns synonyms via WolframAlpha
        elif "synonyms" in query:
            res = client.query(query)
            wolfram_res = next(res.results).text
            speak(f"synonyms for {query} are {wolfram_res}")
            print(wolfram_res)
        # Returns antonyms via WolframAlpha
        elif 'antonyms' in query:
            res = client.query(query)
            wolfram_res = next(res.results).text
            speak(f"synonyms for {query} are {wolfram_res}")
            print(wolfram_res)
        # Opens an app
        elif 'open' in query:
            query = query.replace("open", "")
            speak(f"opening {query}")
            run(query)
        
        #! Keep this at the bottomm
        # Calculates math problem using WolframAlpha
        elif "what's" in query:  
            query = query.replace("what's", "")
            res = client.query(query)                             
            wolfram_res = next(res.results).text
            speak(f"the answer to {query} is {wolfram_res}")
            print(wolfram_res)
        #calculates your math problem using wolfram alpha
        elif 'what is' in query:
            query = query.replace("what is", "")
            res = client.query(query)                             
            wolfram_res = next(res.results).text
            speak(f"the answer to {query} is {wolfram_res}")
            print(wolfram_res)