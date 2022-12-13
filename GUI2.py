import os
import string
import sys
import tkinter as tk
from datetime import time
from tkinter import ttk
from tkinter import *


import Graph as G
import tkintermapview
from geopy import Nominatim

# Graph



routedata.close()


# this is a function which returns the selected combo box item
def getSelectedComboItemStart():
    return StartCity.get()
def btnClickFunction():
        QuickestOutput["text"] = a.QuickestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd())
        CheapOutput["text"] = a.CheapestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd())

        # create a connect path from start to end in the map
        startLocation = geolocator.geocode(getSelectedComboItemStart())
        endLocation = geolocator.geocode(getSelectedComboItemEnd())

        marker_1 = map_widget.set_marker(startLocation.latitude, startLocation.longitude,
                                         text=getSelectedComboItemStart())

        marker_2 = map_widget.set_marker(endLocation.latitude, endLocation.longitude,
                                         text=getSelectedComboItemEnd())

        path_1 = map_widget.set_path(
            [marker_1.position, marker_2.position, (startLocation.latitude, startLocation.longitude),
             (endLocation.latitude, endLocation.longitude)])

        displayFromTo = getSelectedComboItemStart()+" "+"to"+" "+getSelectedComboItemEnd()+":"
        displayQuick = "Quickest Route: "+a.QuickestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd())
        displayCheap = "Cheapest Route: "+a.CheapestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd())
        next = "\n"
        T.configure(state='normal')
        T.insert(INSERT, displayFromTo)
        T.insert(END,next)
        T.insert(INSERT,displayQuick)
        T.insert(END, next)
        T.insert(INSERT,displayCheap)
        T.insert(END, next)
        T.insert(INSERT,next)
        T.configure(state='disabled')




    else:
        QuickestOutput["text"] = "Currently, no routes available from {0} to {1}".format(
            getSelectedComboItemStart(), getSelectedComboItemEnd())
def btnClickFunction():
# Main window configuration
root = Tk()
root.eval('tk::PlaceWindow . center')
root.geometry('650x240')
root.geometry('900x1000')
root.configure(background='#F0F8FF')
root.title('Travel Planner')

# root.resizable(False, False)

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

# create map widget
map_widget = tkintermapview.TkinterMapView(root, width=725, height=450, corner_radius=1)
map_widget.place(x=90, y=530)

map_widget.set_position(40.11527480314763, -75.11050323951898)  # Penn State Abington
map_widget.set_zoom(2)

# Select start and end
StartCity = ttk.Combobox(root, justify='center', values=a.StartGenerateVertexList(), font=('arial', 12, 'normal'),
                         width=17)
StartCity.grid(column=0, row=0, sticky=tk.W, padx=20, pady=20)
# StartCity.grid(column=2, row=0, sticky=tk.W, padx=20, pady=20)
StartCity.place(x=90,y=20)
StartCity.current(0)

EndCity = ttk.Combobox(root, justify='center', values=a.EndGenerateVertexList(), font=('arial', 12, 'normal'),
                       width=17)
EndCity.grid(column=2, row=0, sticky=tk.W, padx=20, pady=20)
# EndCity.grid(column=6, row=0, sticky=tk.W, padx=20, pady=20)
EndCity.place(x=450,y=20)
EndCity.current(0)

# Legend
Label(root, text='→', bg='#F0F8FF', font=('arial', 22, 'normal')).grid(column=1, row=0, padx=25, pady=10)
Label(root, text='Quickest Route', bg='#F0F8FF', font=('arial', 12, 'normal')). \
    grid(column=0, row=1, sticky=tk.W, padx=20, pady=20)
Label(root, text='Cheapest Route', bg='#F0F8FF', font=('arial', 12, 'normal')). \
    grid(column=0, row=2, sticky=tk.W, padx=20, pady=20)
arrowLabel = Label(root, text='→', bg='#F0F8FF', font=('arial', 22, 'normal'))
    # .grid(column=5, row=0, padx=25, pady=10)
arrowLabel.place(x=350,y=10)

quickLabel = Label(root, text='Quickest Route', bg='#F0F8FF', font=('arial', 12, 'normal'))
    # grid(column=2, row=1, sticky=tk.W, padx=20, pady=20)
quickLabel.place(x=90, y =60)

cheapLabel = Label(root, text='Cheapest Route', bg='#F0F8FF', font=('arial', 12, 'normal'))
# grid(column=2, row=2, sticky=tk.W, padx=20, pady=20)
cheapLabel.place(x=90,y= 140)

# Text Box
T = Text(root, height=15,width=80, font=('arial', 12, 'normal'))
T.place(x=90,y=230)



# Quickest path output
QuickestOutput = Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal'))
QuickestOutput.grid(column=1, row=1, columnspan=4, padx=20, pady=20)
# QuickestOutput.grid(column=1, row=1, columnspan=4, padx=20, pady=20, sticky=tk.W)
QuickestOutput.place(x= 250, y=60)

# Cheapest path output
CheapOutput = Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal'))
CheapOutput.grid(column=1, row=2, columnspan=4, padx=20, pady=20)
# CheapOutput.grid(column=1, row=2, columnspan=4, padx=20, pady=20,sticky=tk.W)
CheapOutput.place(x= 250, y=140)

# Search button
Search = Button(root, text='Search Route', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction)
Search.grid(column=3, row=0, padx=5, pady=5)
# Search.grid(column=6, row=0, padx=5, pady=5)
Search.place(x= 700, y= 20)


def restart_program():
    global button
    global label
    global root

    try:
        if (1==1):
            root.destroy()
    finally:
        routedata = open("routedata.txt", "r")
        lines = routedata.readlines()
        records = []
        a = G.Graph()
        for line in lines:
            record = line.split(",")
            records.append(record)

        for i in records:
            Cost = int(i[2])
            Time = int(i[3].replace("\n", ""))
            From = i[0]
            To = i[1]
            a.addEdge(From, To, Time, Cost)

        routedata.close()

        # this is a function which returns the selected combo box item
        def getSelectedComboItemStart():
            return StartCity.get()

        def getSelectedComboItemEnd():
            return EndCity.get()

        # When the button is clicked
        def btnClickFunction():
            if getSelectedComboItemStart() != 'From' or getSelectedComboItemEnd() != 'To':
                if a.QuickestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd()) and \
                        a.CheapestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd()):
                    QuickestOutput["text"] = a.QuickestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd())
                    CheapOutput["text"] = a.CheapestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd())

                    # create a connect path from start to end in the map
                    startLocation = geolocator.geocode(getSelectedComboItemStart())
                    endLocation = geolocator.geocode(getSelectedComboItemEnd())

                    marker_1 = map_widget.set_marker(startLocation.latitude, startLocation.longitude,
                                                     text=getSelectedComboItemStart())

                    marker_2 = map_widget.set_marker(endLocation.latitude, endLocation.longitude,
                                                     text=getSelectedComboItemEnd())

                    path_1 = map_widget.set_path(
                        [marker_1.position, marker_2.position, (startLocation.latitude, startLocation.longitude),
                         (endLocation.latitude, endLocation.longitude)])

                    displayFromTo = getSelectedComboItemStart() + " " + "to" + " " + getSelectedComboItemEnd() + ":"
                    displayQuick = "Quickest Route: " + a.QuickestRoute(getSelectedComboItemStart(),
                                                                        getSelectedComboItemEnd())
                    displayCheap = "Cheapest Route: " + a.CheapestRoute(getSelectedComboItemStart(),
                                                                        getSelectedComboItemEnd())
                    next = "\n"
                    T.configure(state='normal')
                    T.insert(INSERT, displayFromTo)
                    T.insert(END, next)
                    T.insert(INSERT, displayQuick)
                    T.insert(END, next)
                    T.insert(INSERT, displayCheap)
                    T.insert(END, next)
                    T.insert(INSERT, next)
                    T.configure(state='disabled')




                else:
                    QuickestOutput["text"] = "Currently, no routes available from {0} to {1}".format(
                        getSelectedComboItemStart(), getSelectedComboItemEnd())
                    CheapOutput["text"] = "Currently, no routes available from {0} to {1}".format(
                        getSelectedComboItemStart(), getSelectedComboItemEnd())

        print('clicked')

        # Main window configuration
        root = Tk()
        root.eval('tk::PlaceWindow . center')
        root.geometry('900x1000')
        root.configure(background='#F0F8FF')
        root.title('Travel Planner')

        # root.resizable(False, False)

        # Initialize Nominatim API
        geolocator = Nominatim(user_agent="MyApp")

        # create map widget
        map_widget = tkintermapview.TkinterMapView(root, width=725, height=450, corner_radius=1)
        map_widget.place(x=90, y=530)

        map_widget.set_position(40.11527480314763, -75.11050323951898)  # Penn State Abington
        map_widget.set_zoom(2)

        # Select start and end
        StartCity = ttk.Combobox(root, justify='center', values=a.StartGenerateVertexList(),
                                 font=('arial', 12, 'normal'),
                                 width=17)
        # StartCity.grid(column=2, row=0, sticky=tk.W, padx=20, pady=20)
        StartCity.place(x=90, y=20)
        StartCity.current(0)

        EndCity = ttk.Combobox(root, justify='center', values=a.EndGenerateVertexList(), font=('arial', 12, 'normal'),
                               width=17)
        # EndCity.grid(column=6, row=0, sticky=tk.W, padx=20, pady=20)
        EndCity.place(x=450, y=20)
        EndCity.current(0)

        # Legend
        arrowLabel = Label(root, text='→', bg='#F0F8FF', font=('arial', 22, 'normal'))
        # .grid(column=5, row=0, padx=25, pady=10)
        arrowLabel.place(x=350, y=10)

        quickLabel = Label(root, text='Quickest Route', bg='#F0F8FF', font=('arial', 12, 'normal'))
        # grid(column=2, row=1, sticky=tk.W, padx=20, pady=20)
        quickLabel.place(x=90, y=60)

        cheapLabel = Label(root, text='Cheapest Route', bg='#F0F8FF', font=('arial', 12, 'normal'))
        # grid(column=2, row=2, sticky=tk.W, padx=20, pady=20)
        cheapLabel.place(x=90, y=140)

        # Text Box
        T = Text(root, height=15, width=80, font=('arial', 12, 'normal'))
        T.place(x=90, y=230)

        # Quickest path output
        QuickestOutput = Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal'))
        # QuickestOutput.grid(column=1, row=1, columnspan=4, padx=20, pady=20, sticky=tk.W)
        QuickestOutput.place(x=250, y=60)

        # Cheapest path output
        CheapOutput = Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal'))
        # CheapOutput.grid(column=1, row=2, columnspan=4, padx=20, pady=20,sticky=tk.W)
        CheapOutput.place(x=250, y=140)

        # Search button
        Search = Button(root, text='Search Route', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction)
        # Search.grid(column=6, row=0, padx=5, pady=5)
        Search.place(x=700, y=20)

        b = Button(root, text='Reset', bg='#F0F8FF', font=('arial', 12, 'normal'), command=restart_program)
        b.place(x=830, y=20)

        root.mainloop()


b=Button(root, text='Reset', bg='#F0F8FF', font=('arial', 12, 'normal'), command=restart_program)
b.place(x=830, y=20)



root.mainloop()
