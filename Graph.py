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

    def viewVertex(self,target):
        for vertex in self.Graph:
            print(self.Graph[vertex])
            if self.Graph[vertex].key() == target:
                print(self.Graph[vertex])
        """for vertex in self.Graph:
            if self.Graph[vertex] == target:
                print(self.Graph[vertex].value())"""

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
    # a.TestPrint()
    a.viewVertex("Joe")
