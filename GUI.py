from tkinter import *
from tkinter.ttk import *
from Graph import Graph


root = Tk()
root.title("Travel Planner")
root.geometry("500x500")


a = Graph()
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

c = a.CheapestRoute("China", "Japan")
Label(root, text=c).pack()

root.mainloop()
