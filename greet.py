'''Greeting Depending On The Time Of Day'''
import datetime

from speech import speak

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
