import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import *

import tkintermapview
from geopy import Nominatim

import Graph as G


# Graph

a = G.Graph()
a.addVertex("China")
a.addVertex("Russia")
a.addVertex("US")
a.addEdge("China", "US", 2000, 400)
a.addEdge("China", "Italy", 800, 80)
a.addEdge("US", "Russia", 800, 80)
a.addEdge("US", "Japan", 10, 10)
a.addEdge("Germany", "China", 100, 1000)
a.addEdge("Japan", "Russia", 100, 250)
a.addEdge("Japan", "Canada", 1000, 200)




# this is a function which returns the selected combo box item
def getSelectedComboItemStart():
    return StartCity.get()


def getSelectedComboItemEnd():
    return EndCity.get()

def reset():
    btnClickFunction()

# When the button is clicked
def btnClickFunction():
    if getSelectedComboItemStart() != 'From' or getSelectedComboItemEnd() != 'To':
        if a.ShortestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd()) and a.CheapestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd()):
            ShortestOutput["text"] = a.ShortestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd())
            CheapOutput["text"] = a.CheapestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd())

            startLocation = geolocator.geocode(getSelectedComboItemStart())
            endLocation = geolocator.geocode(getSelectedComboItemEnd())

            marker_1 = map_widget.set_marker(startLocation.latitude, startLocation.longitude,
                                             text=getSelectedComboItemStart())
            x= marker_1
            marker_2 = map_widget.set_marker(endLocation.latitude, endLocation.longitude,
                                             text=getSelectedComboItemEnd())
            y = marker_2
            path_1 = map_widget.set_path(
                [marker_1.position, marker_2.position, (startLocation.latitude, startLocation.longitude),
                 (endLocation.latitude, endLocation.longitude)])
            p = path_1
        else:
            ShortestOutput["text"] = "Currently, no routes available from {0} to {1}".format(
                getSelectedComboItemStart(),getSelectedComboItemEnd())
            CheapOutput["text"] = "Currently, no routes available from {0} to {1}".format(
                getSelectedComboItemStart(),getSelectedComboItemEnd())


print('clicked')

# Main window configuration
root = Tk()
root.eval('tk::PlaceWindow . center')
root.geometry('650x700')
root.configure(background='#F0F8FF')
root.title('Travel Planner')

# root.resizable(False, False)

# Select start and end
StartCity = ttk.Combobox(root,  justify='center', values=a.StartGenerateVertexList(), font=('arial', 12, 'normal'), width=15)
StartCity.grid(column=0, row=0, sticky=tk.W, padx=20, pady=20)
StartCity.current(0)

EndCity = ttk.Combobox(root, justify='center', values=a.EndGenerateVertexList(), font=('arial', 12, 'normal'), width=15)
EndCity.grid(column=2, row=0, sticky=tk.W, padx=20, pady=20)
EndCity.current(0)

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

# create map widget
map_widget = tkintermapview.TkinterMapView(root, width=500, height=400, corner_radius=1)
map_widget.place(x=90, y=250)

map_widget.set_position(40.11527480314763, -75.11050323951898)  # Penn State Abington
map_widget.set_zoom(2)

# Legend
Label(root, text='→', bg='#F0F8FF', font=('arial', 22, 'normal')).grid(column=1, row=0, padx=25, pady=10)
Label(root, text='Shortest Route', bg='#F0F8FF', font=('arial', 12, 'normal')). \
    grid(column=0, row=1, sticky=tk.W, padx=20, pady=20)
Label(root, text='Cheapest Route', bg='#F0F8FF', font=('arial', 12, 'normal')). \
    grid(column=0, row=2, sticky=tk.W, padx=20, pady=20)


# Shortest path output
ShortestOutput = Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal'))
ShortestOutput.grid(column=1, row=1, columnspan=4, padx=20, pady=20)

# Cheapest path output
CheapOutput = Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal'))
CheapOutput.grid(column=1, row=2, columnspan=4, padx=20, pady=20)

# Search button
Search = Button(root, text='Search Route', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction)
Search.grid(column=3, row=0, padx=5, pady=5)

Reset = Button(root, text='Reset', bg='#F0F8FF', font=('arial', 12, 'normal'), command= reset)
Reset.grid(column=3, row=2, padx=5, pady=5)
root.mainloop()
