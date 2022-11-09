class Graph:
    def __init__(self):
        self.Graph = {}

    def addVertex(self, city):
        self.Graph[city] = []

    def addEdge(self, start, end, dist, cost):
        self.Graph[start] = self.Graph[start] + [[end, dist, cost]]

    def removeEdge(self, start, end,distance,cost):
        for startPoint in self.Graph.keys():
            if startPoint == start:
                for item in self.Graph[startPoint]:
                    if item == [end,distance,cost]:
                        self.Graph[startPoint].remove(item)

    def viewVertex(self):
        for vertex in self.Graph.keys():
            print(vertex)
    def viewEdge(self,target):
        for vertex in self.Graph.keys():
            if vertex == target:
                print(self.Graph[vertex])


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
    # a.viewVertex()
    # a.viewEdge("Joe")
    a.removeEdge("Joe","Yo",15,13)
    a.TestPrint()