'''Gerald Quick Popup'''
import PySimpleGUI as sg
import keyboard as kb
import datetime
from popupQueries import popupQueries

#pysimplegui layout

#hours
hour = int(datetime.datetime.now().hour)

#returns good morning if time is 0-12
if hour >= 0 and hour<12:
    greeting = "Good Morning"
# Returns good afternoon if time is 12pm - 18pm
elif hour >= 12 and hour<18:
    greeting = "Good Afternoon"  
# Returns good evening if time is 18pm - 12am
else:
    greeting = "Good Evening"

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text(greeting)],
            [sg.Text('What can I do for you today'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

def popup():
    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values[0])
        popupQueries(values[0])

    window.close()



    

        