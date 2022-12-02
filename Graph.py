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

    def generatevertexlist(self):
        list = ['Selected']
        for vertex in self.Graph.keys():
            list.append(vertex)
        return list

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
        if self.__contains__(start_vertex) & self.__contains__(end_vertex):
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

    def CalcDistance(self, start, end):
        if self.__contains__(start) & self.__contains__(end):
            totalCost = 0
            for route in self.Graph[start]:  # Find route
                if route[0] == end:
                    totalCost = totalCost + route[1]
            return totalCost
        else:
            raise Exception("Start and/or vertex does not exist in the graph")

    def routeCost(self, start, end):
        if self.__contains__(start) & self.__contains__(end):
            totalCost = 0
            for route in self.Graph[start]:
                if route[0] == end:
                    totalCost = totalCost + route[2]
            return totalCost
        else:
            raise Exception("Start and/or vertex does not exist in the graph")

    def ShortestRoute(self, start, end):
        if self.__contains__(start) & self.__contains__(end):
            # Find path with the shortest distance
            allPaths = self.find_all_paths(start, end)
            res = []
            for path in allPaths:
                pathDistance = 0
                for i in range(len(path) - 1):
                    pathDistance = pathDistance + self.CalcDistance(path[i], path[i + 1])
                res.append(pathDistance)

            if len(res) != 0:
                TotalDistance = min(res)
                ShortestRoutePath = allPaths[res.index(TotalDistance)]
                # Cost
                cost = 0
                for i in range(len(ShortestRoutePath) - 1):
                    cost = cost + self.routeCost(ShortestRoutePath[i], ShortestRoutePath[i + 1])
                # Print
                path = str(ShortestRoutePath).replace('[', '').replace(']', '').replace("'", '').replace(',', '→')

                return " Total distance {0} miles. Total cost {1} dollars. \nRoute: {2}. ".format(
                    TotalDistance, cost, path)
            else:
                raise Exception("Route does not exist")
        else:
            raise Exception("Start and/or end vertex does not exist in the graph")

    def CheapestRoute(self, start, end):
        if self.__contains__(start) & self.__contains__(end):
            # Find path with the cheapest cost
            allPaths = self.find_all_paths(start, end)
            res = []
            for path in allPaths:
                pathCost = 0
                for i in range(len(path) - 1):
                    pathCost = pathCost + self.routeCost(path[i], path[i + 1])
                res.append(pathCost)

            if len(res) != 0:
                TotalCost = min(res)
                CheapestRoutePath = allPaths[res.index(TotalCost)]
                # Distance
                TotalDistance = 0
                for i in range(len(CheapestRoutePath) - 1):
                    TotalDistance = TotalDistance + self.CalcDistance(CheapestRoutePath[i], CheapestRoutePath[i + 1])
                # Print
                path = str(CheapestRoutePath).replace('[', '').replace(']', '').replace("'", '').replace(',', '→')

                return " Total cost {0} dollars. Total distance {1} miles. \nRoute: {2}".format(
                    TotalCost, TotalDistance, path)
            else:
                raise Exception("Route does not exist")
        else:
            raise Exception("Start and/or end vertex does not exist in the graph")


if __name__ == "__main__":
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

    print(a.ShortestRoute("US", "Italy"))
