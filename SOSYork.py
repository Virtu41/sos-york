"""
Front-end of SOSYork

Date: 20230128
filename: SOSYork.py
Author: Oscar, Nina, Sam
Version: 1.0
"""

import CSVReader  # module
import PySimpleGUI as sg
import pandas as pd
from tabulate import tabulate
import numpy as np

help(sg.Column)
text = ""
WIDTH, HEIGHT = sg.Window.get_screen_size()  # gets screen size
layout = [[sg.Text("Search for service in York")],
          [sg.Checkbox('Colleges: ', default = False)],
          [sg.Checkbox('Departments: ', default = False)],
          [sg.Checkbox('Support: ', default = False)],
          [sg.Input()],  # get input(search bar)
          [sg.Button('Search')],
          [sg.Button('Exit')],  # button to exit
          [sg.Text(text)]
          ]
window = sg.Window('SOS York', layout, margins=(WIDTH / 4, HEIGHT / 4))  # creates window with title and window size
while True:
    event, values = window.read()  # event as buttons, values as search bar values
    if (event == 'Exit') or (event == sg.WIN_CLOSED):  # close program
        break
    if (event == 'Search'):
        window.close()
        print(values)
        # SOSYorkEvent.py
        print(values[3])
        text = CSVReader.csvread(values)
        count = CSVReader.numofresult()
        print(count)
        column1 = [
            [sg.Text(f'Scrollable{i}')] for i in range(count)
        ]
        layout = [[sg.Text("Search for service in York")],
                  [sg.Checkbox('Colleges: ', default=False)],
                  [sg.Checkbox('Departments: ', default=False)],
                  [sg.Checkbox('Support: ', default=False)],
                  [sg.Input()],  # get input(search bar)
                  [sg.Button('Search')],
                  [sg.Button('Exit')],  # button to exit
                  [sg.Text(text)],
                  [sg.Column(column1, scrollable=True,  vertical_scroll_only=True)],
                  ]
        window = sg.Window('SOS York', layout, margins=(WIDTH / 4, HEIGHT / 4))


window.close()
