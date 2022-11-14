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
    a.addVertex("China")
    a.addVertex("Russia")
    a.addVertex("US")
    a.addEdge("China", "US", 2000, 150)
    a.addEdge("China", "Russia", 800, 80)
    a.TestPrint()
    a.removeEdge("China","US",2000,150)
    a.TestPrint()

