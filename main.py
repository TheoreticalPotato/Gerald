#Importing of libraries and definition of key variables
import subprocess 
import wolframalpha # pip install wolframaplha
# wolfram alpha client key
client = wolframalpha.Client("KT955E-4QYKLV4VE5")
import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speech_recognition
import datetime # pip install datetime
import wikipedia # pip install wikipedia
import webbrowser # pip install webbrowser
from AppOpener import run
import pyttsx3 # pip install pyttsx3

# text to speech setup, engine,
engine = pyttsx3.init('sapi5')                    
engine.setProperty('rate', 230)     
engine.setProperty('volume', 1.0)    
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[0].id)
currentTime = datetime.datetime.now()

#@param 'audio' speaks the words put in the parameter
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# greets you depending on the time of day
def greeting():
    hour = int(datetime.datetime.now().hour)
    # if it's 12am - 12pm: good morning
    if hour >= 0 and hour<12:
        speak("Good Morning")
    # if it's 12pm - 18pm: good afternoon
    elif hour >= 12 and hour<18:
        speak("Good Afternoon")  
    # if it's 18pm - 12am: good evening
    else:
        speak("Good Evening") 

#takes your command
def takeCommand():
    
    r = sr.Recognizer()
    # sets mic as the default system one
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    # tries to do recognize your voice
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    # if it doesnt recognize your voice
    except Exception as e:
        print(e)   
        print("Unable to recognize your goofy ass voice") 
        return "None"
    # replaces 'gerald' and 'hey' so it doesnt mess up the command
    if 'Gerald' or 'hey Gerald' in query:
        query = query.replace("Gerald", "")
        query = query.replace("hey", "")
        return query
    # if the command doesnt include 'gerald' then it doesnt register
    else:
        query = ""
        return query 

# acual script part: reads what you say and reacts accordingly
if __name__ == '__main__':
    greeting()
    speak("what can I do for you today")

    while True:
        query = takeCommand()
        # wikipedia search
        if 'wikipedia' in query:  
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            wiki_ans = wikipedia.summary(query, sentences = 2)
            speak(wiki_ans)
        # tells you the time
        elif 'time' in query:   
            speak("The time is now: %s:%s" % (currentTime.hour, currentTime.minute))
        # kills gerald
        elif 'exit' in query:
            speak("killing gerald")
            speak("what a world. what a world.")
            print("you have killed Gerald, you monster")
            exit()
        # calculates your math problem using wolfram alpha
        elif 'calculate' in query:  
            query = query.replace("calculate", "")
            res = client.query(query)                             
            wolfram_res = next(res.results).text
            speak(f"the answer to {query} is {wolfram_res}")
            print(wolfram_res)
        # searches default browser
        elif 'search' in query:     
            query = query.replace("search", "")
            speak("searching on the web")
            webbrowser.open(query)
        # opens taiwan news
        elif 'news' in query:       
            speak("opening taiwan news")
            webbrowser.open("taiwannews.com.tw")
        # shuts down windows computer
        elif 'shutdown' in query:
            speak("shutting down your computer")
            subprocess.call('shutdown /s')
            exit()
        # restarts windows computer
        elif "restart" in query:        
            subprocess.call(["shutdown", "/r"])
            exit()
        # uses wolfram alpha to tell you the weather at your current location
        elif "weather" in query:
            res = client.query(query)                             
            wolfram_res = next(res.results).text
            speak(f"the weather is currently {wolfram_res}")
            print(wolfram_res)
        # uses wolfram alpha to define your word
        elif "definition" in query:
            query = query.replace("define", "")
            res = client.query(query)                             
            wolfram_res = next(res.results).text
            speak(f"the definition of {query} is {wolfram_res}")
            print(wolfram_res)
        # uses wolfram alpha to give you synonyms for your word
        elif "synonyms" in query:
            res = client.query(query)
            wolfram_res = next(res.results).text
            speak(f"synonyms for {query} are {wolfram_res}")
            print(wolfram_res)
        # uses wolfram alpha to give you antonyms for your word
        elif 'antonyms' in query:
            res = client.query(query)
            wolfram_res = next(res.results).text
            speak(f"synonyms for {query} are {wolfram_res}")
            print(wolfram_res)
        # opens an app on your windows computer
        elif 'open' in query:
            query = query.replace("open", "")
            speak(f"opening {query}")
            run(query)
        
        #* Keep this at the bottomm
        # calculates your math problem using wolfram alpha
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