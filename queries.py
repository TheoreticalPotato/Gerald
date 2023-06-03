'''Converts The Command Into An Action'''
import wikipedia
import webbrowser as wb
from AppOpener import *
import subprocess
import datetime
import wolframalpha
# WolframAlpha client key
client = wolframalpha.Client("wolframalhpa api key")

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
            wb.open(query)

        # Wikipedia search
        elif 'wikipedia' in query:  
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            wiki_ans = wikipedia.summary(query, sentences = 2)
            speak(wiki_ans)

        # Opens Taiwan News in browser
        elif 'news' in query:       
            speak("opening taiwan news")
            wb.open("taiwannews.com.tw")



    #TODO Chatgpt, Reddit, Google Docs, Google Slides, Google Sheets, youtube
    #* System operations
        # Opens an app or website
        elif 'open' in query:
            query = query.replace("open", "")

            # google drive
            if 'Google Drive' in query:
                speak('opening google drive')
                wb.open('https://drive.google.com', new=0)

            # canvas
            elif 'canvas' in query:
                speak('opening canvas')
                wb.open('https://taipeiamericanschool.instructure.com', new=0)
            
            # gmail
            elif 'Gmail' in query:
                speak('opening gmail')
                wb.open('https://gmail.com')

            # chatgpt
            elif 'chat GPT' in query:
                speak('opening chat gpt')
                wb.open('https://chat.openai.com')
            
            # reddit
            elif 'Reddit' in query:
                speak('opening reddit')
                wb.open('https://reddit.com')

            # Google Docs
            elif 'Google Docs' in query:
                speak('opening google docs')
                wb.open('https://docs.google.com')
            
            # Google Slides
            elif 'Google Slides' in query:
                speak('openin google slides')
                wb.open('https://slides.google.com')
            
            # google sheets
            elif 'Google Sheets' in query:
                speak('opening google sheets')
                wb.open('https://sheets.google.com')
            
            # YouTube
            elif 'YouTube' in query:
                speak('opening youtube')
                wb.open('https://youtube.com')

            # opens computer application if it cant
            else:
                try: 
                    open(query, match_closest=True)
                    speak(f'opening {query}')
                    
                except: 
                    speak('sorry, I cannot find that application on your computer')

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

        # lights
        elif 'turn on' in query:
            query = query.replace("turn on ", "")
            speak(f'turning on {query} to full brightness')
            setFull(query)

        elif 'turn off' in query:
            query = query.replace("turn off ", "")
            speak(f'turning off  {query}')
            setOff(query)
        
        elif 'set scene PC' in query:
            query = query.replace("set scene PC ", "")
            speak(f'setting pc scene to {query}')
            try:
                setScene('PC', query)
            except:
                speak('sorry, that is not an avalible scene')
            
            

    #* WolframAlpha
    # uses wolframalpha as a backup
        # elif 'what' or "what's" or "define" or "synonyms" or "antonyms" or 'weather' or 'calculate' in query:
        #     res = client.query(query)                             
        #     wolfram_res = next(res.results).text
        #     speak(wolfram_res)
        #     print(wolfram_res)