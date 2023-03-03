'''Converts The Command Into An Action'''
import wikipedia
import webbrowser
from AppOpener import run
import subprocess
import datetime
import wolframalpha
# WolframAlpha client key
client = wolframalpha.Client("KT955E-4QYKLV4VE5")

import PySimpleGUI as sg

def popupQueries(question):
    while True:
        currentTime = datetime.datetime.now()

    #* Searches
        # Searches in browser
        if 'search' in question:     
            question = question.replace("search", "")
            sg.Popup("searching on the web")
            webbrowser.open(question)

        # Wikipedia search
        elif 'wikipedia' in question:  
            sg.Popup("searching wikipedia")
            question = question.replace("wikipedia", "")
            wiki_ans = wikipedia.summary(question, sentences = 2)
            sg.Popup(wiki_ans)

        # Opens Taiwan News in browser
        elif 'news' in question:       
            sg.Popup("opening taiwan news")
            webbrowser.open("taiwannews.com.tw")


    #* System operations
        # Opens an app
        elif 'open' in question:
            question = question.replace("open", "")
            sg.Popup(f"opening {question}")
            run(question)

        # Reboots computer
        elif "restart" in question:        
            subprocess.call(["shutdown", "/r"])
            exit()

        # Shuts down computer
        elif 'shutdown' in question:
            sg.Popup("shutting down your computer")
            subprocess.call('shutdown /s')
            exit()

        # Terminates program
        elif 'exit' in question:
            sg.Popup("killing gerald")
            sg.Popup("what a world. what a world.")
            print("you have killed Gerald, you monster")
            exit()
        
        # Returns time
        elif 'time' in question:   
            sg.Popup("The time is now: %s:%s" % (currentTime.hour, currentTime.minute))

    #* WolframAlpha
    #uses wolframlaph as a backup
        else:
            question = question.replace("define", "")
            res = client.query(question)                             
            wolfram_res = next(res.results).text
            sg.Popup(wolfram_res)
            print(wolfram_res)