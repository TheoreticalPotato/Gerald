'''Main'''
from greet import greeting
from diction import takeCommand
from speech import speak
from queries import queries
import keyboard as kb
from popup import popup

if __name__ == '__main__':
    greeting() # Greets user
    speak("what can I do for you today")
    queries() # Listens for queries
    
    if kb.is_pressed('right shift'):
        popup()