import wikipedia
import webbrowser
from AppOpener import run
import subprocess
import datetime
import wolframalpha
# WolframAlpha client key
client = wolframalpha.Client("<API KEY>")

from diction import takeCommand
from speech import speak

def queries():
    while True:
        query = takeCommand()
        currentTime = datetime.datetime.now()

    #* Searches
        # Searches in browser
        if 'search' in query:     
            query = query.replace("search", "")
            speak("searching on the web")
            webbrowser.open(query)

        # Wikipedia search
        elif 'wikipedia' in query:  
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            wiki_ans = wikipedia.summary(query, sentences = 2)
            speak(wiki_ans)

        # Opens Taiwan News in browser
        elif 'news' in query:       
            speak("opening taiwan news")
            webbrowser.open("taiwannews.com.tw")


    #* System operations
        # Opens an app
        elif 'open' in query:
            query = query.replace("open", "")
            speak(f"opening {query}")
            run(query)

        # Reboots computer
        elif "restart" in query:        
            subprocess.call(["shutdown", "/r"])
            exit()

        # Shuts down computer
        elif 'shutdown' in query:
            speak("shutting down your computer")
            subprocess.call('shutdown /s')
            exit()

        # Terminates program
        elif 'exit' in query:
            speak("killing gerald")
            speak("what a world. what a world.")
            print("you have killed Gerald, you monster")
            exit()
        
        # Returns time
        elif 'time' in query:   
            speak("The time is now: %s:%s" % (currentTime.hour, currentTime.minute))


    #* WolframAlpha
        # Returns weather at current location via WolframAlpha
        elif "weather" in query:
            res = client.query(query)                             
            wolfram_res = next(res.results).text
            speak(f"the weather is currently {wolfram_res}")
            print(wolfram_res)

        #* Vocabulary
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

        #* Math
        # Calculates math problem via WolframAlpha
        elif 'calculate' in query:  
            query = query.replace("calculate", "")
            res = client.query(query)                             
            wolfram_res = next(res.results).text
            speak(f"the answer to {query} is {wolfram_res}")
            print(wolfram_res)

        #! Keep this at the bottom
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