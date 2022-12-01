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


# this is a function which returns the selected combo box item
def getSelectedComboItemEnd():
    return EndCity.get()


"""# this is a function to get the user input from the text input box
def getInputBoxValue():
    userInput = tInput.get()
    return userInput"""


# this is the function called when the button is clicked
def btnClickFunction():
    if getSelectedComboItemStart() != 'Selected' or getSelectedComboItemEnd() != 'Selected':
        #print(a.ShortestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd()))
        ShortestOutput["text"] = a.ShortestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd())
        CheapOutput["text"] = a.CheapestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd())
        print('clicked')


root = Tk()
root.eval('tk::PlaceWindow . center')
root.resizable(False, False)

# This is the section of code which creates the main window
root.geometry('435x250')
root.configure(background='#F0F8FF')
root.title('Travel Planner')

# This is the section of code which creates a combo box

StartCity = ttk.Combobox(root, values=a.generatevertexlist(), font=('arial', 12, 'normal'), width=10)
StartCity.place(x=20, y=30)
StartCity.current(0)

EndCity = ttk.Combobox(root, values=a.generatevertexlist(), font=('arial', 12, 'normal'), width=10)
EndCity.place(x=175, y=30)
EndCity.current(0)

# This is the section of code which creates a label
Label(root, text='→', bg='#F0F8FF', font=('arial', 22, 'normal')).place(x=135, y=20)

Label(root, text='Shortest Route', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=20, y=80)

Label(root, text='Cheapest Route', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=20, y=130)

# Cheapest
CheapOutput = Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal'))


ShortestOutput = Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal'))

"""# This is the section of code which creates a text input box
tInput = Entry(root)
tInput.place(x=166, y=9)"""

# This is the section of code which creates a button
Button(root, text='Search Route', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=305,
                                                                                                              y=25)
ShortestOutput.place(x=175, y=80)
CheapOutput.place(x=175, y=130)

root.mainloop()
