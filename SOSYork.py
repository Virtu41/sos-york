"""
Front-end of sos-york

Date: 20230128
filename: SOSYork.py
Author: Oscar, Nina, Sam
Version: 1.0
"""

import PySimpleGUI as sg

WIDTH, HEIGHT = sg.Window.get_screen_size()  # gets screen size
layout = [[sg.Text("Search for service in York")],
          [sg.Input()],  # get input(search bar)
          [sg.Button('Search')],
          [sg.Button('Exit')]  # button to exit
          ]
window = sg.Window('SOS York', layout, margins=(WIDTH / 4, HEIGHT / 4))  # creates window with title and window size
while True:
    event, values = window.read()  # event as buttons, values as search bar values
    print(event, values)
    if (event == 'Exit') or (event == sg.WIN_CLOSED):  # close program
        break
    if (event == 'Search'):
        # SOSYorkEvent.py
        print('ok')
        searchWindow = sg.Window('SOS York', layout, margins=(WIDTH / 4, HEIGHT / 4))

window.close()
