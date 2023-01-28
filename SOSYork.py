"""
Searches for York undergraduate contacts based on name of the service

Date: 20230128
filename: SOSYork.py
Author: Oscar, Nina, Sam
Version: 1.0
"""

import CSVReader  # module
import PySimpleGUI as sg

text = ""
WIDTH, HEIGHT = sg.Window.get_screen_size()  # gets screen size
sg.set_options(font=("Courier New", 10))
layout = [[sg.Text("Search for service in York")],
          [sg.Input()],  # get input(search bar)
          [sg.Button('Search')], # button to search
          [sg.Button('Exit')],  # button to exit
          ]
window = sg.Window('SOS York', layout, margins=(WIDTH / 5, HEIGHT / 5))  # creates window with title and window size
while True:
    event, values = window.read()  # event as buttons, values as search bar values
    if (event == 'Exit') or (event == sg.WIN_CLOSED):  # close program
        break
    if (event == 'Search'):
        window.close()
        text = CSVReader.csvread(values)
        count = CSVReader.numofresult()
        csv = [
            [sg.Text(text)]
        ]
        layout = [[sg.Text("Search for service in York")],  # add text
                  [sg.Input()],  # get input(search bar)
                  [sg.Button('Search')],
                  [sg.Button('Exit')],  # button to exit
                  [sg.Text(f"Searches for {values[0]}: {count}")],  # counts amount of results appeared
                  [sg.Multiline(text, size=(int(WIDTH/10), int(HEIGHT/30)), no_scrollbar=False, horizontal_scroll=True, visible=True)]  # used to create table and horizontal and vertical scrollbar
                  ]
        window = sg.Window('SOS York', layout)  # change window display

window.close()  # close window
