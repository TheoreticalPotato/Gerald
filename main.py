'''Main'''
from greet import greeting
from diction import takeCommand
from speech import speak
from queries import queries
import keyboard as kb
from popup import popup
from multiprocessing import Process

if __name__ == '__main__':

    #ques and runs the greeting
    funcGreeting = Process(target = greeting)
    funcGreeting.start()
    
    #ques and runs queries
    funcQueries = Process(target = queries)
    funcQueries.start()

    #ques and runs the popup when you press right shift
    #! currently has an error and I dont understand it
    funcPopup = Process(target = popup)
    while True:
        if kb.is_pressed('right shift'):
            funcPopup.start()