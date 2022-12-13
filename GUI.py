from tkinter import ttk
from tkinter import *

import Graph as G
import tkintermapview
from geopy import Nominatim


# Graph
def main():
    # Get data
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

    def btnClickFunction():
        if getSelectedComboItemStart() != 'From' or getSelectedComboItemEnd() != 'To':
            if a.QuickestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd()) and \
                    a.CheapestRoute(getSelectedComboItemStart(), getSelectedComboItemEnd()):

                # Draw line from start to end in the map
                startLocation = geolocator.geocode(getSelectedComboItemStart())
                endLocation = geolocator.geocode(getSelectedComboItemEnd())

                marker_1 = map_widget.set_marker(startLocation.latitude, startLocation.longitude,
                                                 text=getSelectedComboItemStart())

                marker_2 = map_widget.set_marker(endLocation.latitude, endLocation.longitude,
                                                 text=getSelectedComboItemEnd())

                path_1 = map_widget.set_path(
                    [marker_1.position, marker_2.position, (startLocation.latitude, startLocation.longitude),
                     (endLocation.latitude, endLocation.longitude)])

                displayFromTo = "From " + getSelectedComboItemStart() + " " + "to" + " " + getSelectedComboItemEnd()
                displayQuick = "\nQuickest Route: \n" + a.QuickestRoute(getSelectedComboItemStart(),
                                                                        getSelectedComboItemEnd())
                displayCheap = "\nCheapest Route: \n" + a.CheapestRoute(getSelectedComboItemStart(),
                                                                        getSelectedComboItemEnd())

                T.configure(state='normal')
                T.delete("1.0", "end")
                T.insert(INSERT, displayFromTo, "\n")
                T.insert(END, "\n")
                T.insert(INSERT, displayQuick, "\n")
                T.insert(END, "\n")
                T.insert(INSERT, displayCheap, "\n")
                T.insert(END, "\n")
                T.insert(INSERT, "\n")
                T.configure(state='disabled')

            else:
                Text = "Currently, no routes available from {0} to {1}".format(
                    getSelectedComboItemStart(), getSelectedComboItemEnd())
                T.configure(state='normal')
                T.delete("1.0", "end")
                T.insert(INSERT, Text)
                T.insert(INSERT, "\n")
                T.configure(state='disabled')

    def restart_program():
        root.destroy()
        main()

    # Main window configuration
    root = Tk()
    # root.eval('tk::PlaceWindow . center')
    root.geometry('1000x600')
    root.configure(background='#F0F8FF')
    root.title('Travel Planner')

    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="MyApp")

    # Select start and end
    StartCity = ttk.Combobox(root, justify='center', values=a.StartGenerateVertexList(), font=('arial', 12, 'normal'),
                             width=17)
    StartCity.place(x=80, y=20)
    StartCity.current(0)

    EndCity = ttk.Combobox(root, justify='center', values=a.EndGenerateVertexList(), font=('arial', 12, 'normal'),
                           width=17)
    EndCity.place(x=450, y=20)
    EndCity.current(0)

    # Legend
    arrowLabel = Label(root, text='→', bg='#F0F8FF', font=('arial', 22, 'normal'))
    arrowLabel.place(x=330, y=10)

    # create map widget
    map_widget = tkintermapview.TkinterMapView(root, width=842, height=300, corner_radius=1)
    map_widget.place(x=80, y=270)

    map_widget.set_position(40.11527480314763, -75.11050323951898)  # Penn State Abington
    map_widget.set_zoom(2)

    # Text Box
    T = Text(root, width=93, height=10, font=('arial', 12, 'normal'))
    T.place(x=80, y=60)

    # Search button
    Search = Button(root, text='Search Route', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction)
    Search.place(x=730, y=20)

    b = Button(root, text='Reset', bg='#F0F8FF', font=('arial', 12, 'normal'), command=restart_program)
    b.place(x=865, y=20)

    root.mainloop()


if __name__ == "__main__":
    main()
