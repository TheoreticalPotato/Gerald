'''Gerald Quick Popup'''
import PySimpleGUI as sg
import keyboard as kb
import greet
import datetime

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

layout = [ [sg.Text(greeting)],
        [sg.Text('What can I do for you?')], [sg.InputText()],
        [sg.Button('ok')], [sg.Button('Cancel)')]]

window = sg.Window('Gerald', layout)

def popup():
    while True: 
        sg.Window(layout)
    
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel' or kb.is_pressed('escape'): # if user closes window or clicks cancel
            break
        print('You entered ', values[0])
    

        