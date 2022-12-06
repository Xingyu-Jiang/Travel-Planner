import tkinter as tk
from tkinter import ttk
from tkinter import *
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


# When the button is clicked
def btnClickFunction():
    if getSelectedComboItemStart() != 'Selected' or getSelectedComboItemEnd() != 'Selected':
        ShortestOutput["text"] = a.ShortestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd())
        CheapOutput["text"] = a.CheapestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd())
        print('clicked')


# Main window configuration
root = Tk()
root.eval('tk::PlaceWindow . center')
root.geometry('615x240')
root.configure(background='#F0F8FF')
root.title('Travel Planner')

# root.resizable(False, False)

# Select start and end
StartCity = ttk.Combobox(root, values=a.generatevertexlist(), font=('arial', 12, 'normal'), width=15)
StartCity.grid(column=0, row=0, sticky=tk.W, padx=20, pady=20)
StartCity.current(0)

EndCity = ttk.Combobox(root, values=a.generatevertexlist(), font=('arial', 12, 'normal'), width=15)
EndCity.grid(column=2, row=0, sticky=tk.W, padx=20, pady=20)
EndCity.current(0)

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
root.mainloop()
