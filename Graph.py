class Graph:
    def __init__(self):
        self.Graph = {}

    def addVertex(self, city):  # Create new key in the Graph dictionary as a new vertex.
        self.Graph[city] = []  # New vertex with empty value

    def __contains__(self, item):
        return item in self.Graph.keys()

    def addEdge(self, start, end, dist, cost):  # Set the edges and give weights
        if start not in self.Graph:  # If the start vertex does not exist in the graph
            self.addVertex(start)  # Adding in the start vertex
        if end not in self.Graph:  # If the end vertex does not exist in the graph
            self.addVertex(end)  # Adding in the end vertex
        # Set the edge in the format of destination, distance, cost
        self.Graph[start] = self.Graph[start] + [[end, dist, cost]]

    def removeEdge(self, start, end):
        for vertex in self.Graph.keys():  # Check all vertex in the graph
            if vertex == start:  # Find the vertex to delete edge from
                for item in self.Graph[vertex]:  # Check all the edge the targeted vertex have
                    if item[0] == end:  # If the edge exist
                        self.Graph[vertex].remove(item)  # Remove the edge
                    else:  # If the edge does not exist
                        raise Exception("No such edge")

    def viewVertices(self):
        for vertex in self.Graph.keys():  # Print all vertices
            print(vertex)

    def viewEdges(self, target):
        for vertex in self.Graph.keys():  # Search for the target vertex
            if vertex == target:
                for item in self.Graph[vertex]:  # Return all the edge such vertex is connected to
                    print("From", vertex, "to", item[0],
                          "\nDistance:", item[1], "miles",
                          "\nCost", item[2], "dollars\n")

    def TestPrint(self):
        for keys, values in self.Graph.items():
            print(keys, values)

    def find_all_paths(self, start_vertex, end_vertex, path=None):
        if a.__contains__(start_vertex) & a.__contains__(end_vertex):
            if path is None:
                path = []
            path = path + [start_vertex]
            if start_vertex == end_vertex:
                return [path]

            # If the start vertex is no in Graph
            vertex = []
            for x in self.Graph.keys():
                vertex.append(x)

            if start_vertex not in vertex:
                return []
        else:
            raise Exception("Start and/or end vertex does not exist in the graph")

        # If the start vertex is in graph
        paths = []
        for vertex in self.Graph[start_vertex]:
            if vertex[0] not in path:
                extended_paths = self.find_all_paths(vertex[0], end_vertex, path)
                for p in extended_paths:
                    paths.append(p)

        return paths

    def Distance(self, start, end):
        if a.__contains__(start) & a.__contains__(end):
            totalCost = 0
            for route in self.Graph[start]:  # Find route
                if route[0] == end:
                    totalCost = totalCost + route[1]
            return totalCost
        else:
            raise Exception("Start and/or vertex does not exist in the graph")

    def routeCost(self, start, end):
        if a.__contains__(start) & a.__contains__(end):
            totalCost = 0
            for route in self.Graph[start]:
                if route[0] == end:
                    totalCost = totalCost + route[2]
            return totalCost
        else:
            raise Exception("Start and/or vertex does not exist in the graph")

    def ShortestRoute(self, start, end):
        if a.__contains__(start) & a.__contains__(end):
            allpath = self.find_all_paths(start, end)
            res = []
            for path in allpath:
                pathCost = 0
                for i in range(len(path) - 1):
                    pathCost = pathCost + self.Distance(path[i], path[i + 1])
                res.append(pathCost)
            if len(res) != 0:
                return allpath[res.index(min(res))], min(res)
            else:
                raise Exception("Route does not exist")
        else:
            raise Exception("Start and/or end vertex does not exist in the graph")

    def CheapestRoute(self, start, end):
        if a.__contains__(start) & a.__contains__(end):
            allpath = self.find_all_paths(start, end)
            res = []
            for path in allpath:
                pathCost = 0
                for i in range(len(path) - 1):
                    pathCost = pathCost + self.routeCost(path[i], path[i + 1])
                res.append(pathCost)
            if len(res) != 0:
                return allpath[res.index(min(res))], min(res)
            else:
                raise Exception("Route does not exist")
        else:
            raise Exception("Start and/or end vertex does not exist in the graph")


if __name__ == "__main__":
    a = Graph()
    a.addVertex("China")
    a.addVertex("Russia")
    a.addVertex("US")
    a.addEdge("China", "US", 2000, 150)
    a.addEdge("China", "meowcity", 800, 80)
    a.addEdge("US", "Russia", 800, 80)
    a.addEdge("US", "DogCity", 10, 10)
    a.addEdge("CatCity", "China", 100000, 100000)
    a.addEdge("DogCity", "Russia", 10, 20)
    a.TestPrint()
    print("--------")
    print(a.ShortestRoute("China", "meowcity"))
    print(a.Distance("China", "meowcity"))
