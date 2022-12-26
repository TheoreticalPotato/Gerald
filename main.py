from greet import greeting
from diction import takeCommand
from speech import speak
from queries import queries

if __name__ == '__main__':
    greeting() # Greets user
    speak("what can I do for you today")
    queries() # Listens for queries