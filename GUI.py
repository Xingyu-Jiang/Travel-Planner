import tkinter as tk
from tkinter import ttk
from tkinter import *
import Graph as G

# Graph

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

        else:
            QuickestOutput["text"] = "Currently, no routes available from {0} to {1}".format(
                getSelectedComboItemStart(), getSelectedComboItemEnd())
            CheapOutput["text"] = "Currently, no routes available from {0} to {1}".format(
                getSelectedComboItemStart(), getSelectedComboItemEnd())


print('clicked')

# Main window configuration
root = Tk()
root.eval('tk::PlaceWindow . center')
root.geometry('615x240')
root.configure(background='#F0F8FF')
root.title('Travel Planner')

# root.resizable(False, False)

# Select start and end
StartCity = ttk.Combobox(root, justify='center', values=a.StartGenerateVertexList(), font=('arial', 12, 'normal'),
                         width=15)
StartCity.grid(column=0, row=0, sticky=tk.W, padx=20, pady=20)
StartCity.current(0)

EndCity = ttk.Combobox(root, justify='center', values=a.EndGenerateVertexList(), font=('arial', 12, 'normal'), width=15)
EndCity.grid(column=2, row=0, sticky=tk.W, padx=20, pady=20)
EndCity.current(0)

# Legend
Label(root, text='→', bg='#F0F8FF', font=('arial', 22, 'normal')).grid(column=1, row=0, padx=25, pady=10)
Label(root, text='Quickest Route', bg='#F0F8FF', font=('arial', 12, 'normal')). \
    grid(column=0, row=1, sticky=tk.W, padx=20, pady=20)
Label(root, text='Cheapest Route', bg='#F0F8FF', font=('arial', 12, 'normal')). \
    grid(column=0, row=2, sticky=tk.W, padx=20, pady=20)

# Quickest path output
QuickestOutput = Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal'))
QuickestOutput.grid(column=1, row=1, columnspan=4, padx=20, pady=20)

# Cheapest path output
CheapOutput = Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal'))
CheapOutput.grid(column=1, row=2, columnspan=4, padx=20, pady=20)

# Search button
Search = Button(root, text='Search Route', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction)
Search.grid(column=3, row=0, padx=5, pady=5)

root.mainloop()