class Graph:
    def __init__(self):
        self.Graph = {}

    def addVertex(self, city):
        self.Graph[city] = []

    def addEdge(self, start, end, dist, cost):
        self.Graph[start] = self.Graph[start] + [[end, dist, cost]]

    def removeEdge(self, start, end):
        for i in self.Graph:
            if i == start:
                print(self.Graph[start])
    def viewvertex(self):
        for vertex in Graph:
            print(vertex)

    def TestPrint(self):
        print(self.Graph)


if __name__ == "__main__":
    a = Graph()
    a.addVertex("Joe")
    a.addVertex("Yo")
    a.addVertex("Hi")
    a.addEdge("Joe", "Yo", 15, 13)
    a.addEdge("Joe", "Hi", 36, 80)
    # a.removeEdge("Joe","Yo")
    a.TestPrint()
