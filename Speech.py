
# 28/03/23

import PySimpleGUI as sg
import pyttsx3
layout = [
    [sg.Text("Text: "), sg.InputText(key="INPUT")],
    [sg.Button("Speak", key="SPEAK")],
    [sg.Text("Select Voice type: "), sg.OptionMenu(values=['Male', 'Female'], key="VOICE")]
]

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id) 

window = sg.Window("Text to Speech App", layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
        
    if event == 'SPEAK':
        text = values['INPUT']
        voice = values['VOICE']
        
        if voice == 'Male':
            speaker.setProperty('voice', voices[0].id)
        elif voice == 'Female':
            speaker.setProperty('voice', voices[1].id)
            
        speaker.say(text)
        speaker.runAndWait()