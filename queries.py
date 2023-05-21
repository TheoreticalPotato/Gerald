'''Converts The Command Into An Action'''
import wikipedia
import webbrowser
from AppOpener import run
import subprocess
import datetime
import wolframalpha
# WolframAlpha client key
client = wolframalpha.Client("KT955E-4QYKLV4VE5")

from diction import takeCommand
from speech import speak
from phueCommands import *
import phueCommands as phue 

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

        #! puts space before pc idk why help ahhhhh
        elif 'turn on' in query:
            query = query.replace('turn on ', '')
            speak(f'turning on {query} to full brightness')
            if query[1] == ' ':
                query.replace(" ", "")
            setFull(query)

        elif 'turn off' in query:
            query = query.replace('turn off ', '')
            speak(f'turning off  {query}')
            if query[1] == ' ':
                query.replace(" ", "")
            print (query)
            setOff(query)

    #* WolframAlpha
    # uses wolframalpha as a backup
        else:
            query = query.replace("define", "")
            res = client.query(query)                             
            wolfram_res = next(res.results).text
            speak(wolfram_res)
            print(wolfram_res)