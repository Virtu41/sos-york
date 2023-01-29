"""
Searches for York undergraduate contacts based on name of the service

Date: 20230128
filename: SOSYork.py
Author: Oscar, Nina, Sam
Version: 1.0
"""

import CSVReader  # module
import PySimpleGUI as sg


def searching():
    global window, layout, values

    window.close()
    text = CSVReader.csvread(values)  # receive string table
    count = CSVReader.numofresult()  # number of results
    layout = [[sg.Text("SOS York", font = 20)],
              [sg.Text("Search for service, email or phone number")],
              [sg.Input()],  # get input(search bar)
              [sg.Button('Search')],
              [sg.Button('Show all', tooltip = "Shows all services")],
              [sg.Button('Exit')],  # button to exit
              [sg.Text(f"Searches for {values[0]}: {count}")],  # counts amount of results appeared
              [sg.Multiline(text, size=(int(WIDTH / 10), int(HEIGHT / 50)), no_scrollbar=False, horizontal_scroll=True,
                        visible=True)]  # used to create table and horizontal and vertical scrollbar
          ]
    window = sg.Window('SOS York', layout, finalize=True)  # change window display
    window.bind("<Return>", "_Enter")

WIDTH, HEIGHT = sg.Window.get_screen_size()  # gets screen size
sg.set_options(font=("Courier New", 10))
sg.theme('LightBrown3')
layout = [[sg.Text("SOS York", font = 20)],
          [sg.Text("Search for service, email or phone number")],
          [sg.Input()],  # get input(search bar)
          [sg.Button('Search')],  # button to search
          [sg.Button('Show all', tooltip = "Shows all services")],
          [sg.Button('Exit')]  # button to exit
          ]
window = sg.Window('SOS York', layout, finalize = True)  # creates window with title and window size
window.bind("<Return>", "_Enter")
while True:
    event, values = window.read()  # event as buttons, values as search bar values
    if (event == 'Exit') or (event == sg.WIN_CLOSED):  # close program
        break
    if ((event == 'Search' or event == "_Enter") and len(values[0]) > 0):
        searching()
    if (event== 'Show all'):
        values[0] = ""
        searching()

window.close()  # close window
