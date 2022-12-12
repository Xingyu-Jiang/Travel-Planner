class Graph:
    def __init__(self):
        self.Graph = {}

    def addVertex(self, city):  # Create new key in the Graph dictionary as a new vertex.
        self.Graph[city] = []  # New vertex with empty value

    def __contains__(self, item):
        return item in self.Graph.keys()

    def addEdge(self, start, end, time, cost):  # Set the edges and give weights
        if start not in self.Graph:  # If the start vertex does not exist in the graph
            self.addVertex(start)  # Adding in the start vertex
        if end not in self.Graph:  # If the end vertex does not exist in the graph
            self.addVertex(end)  # Adding in the end vertex
        # Set the edge in the format of destination, time, cost
        self.Graph[start] = self.Graph[start] + [[end, time, cost]]

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

    def StartGenerateVertexList(self):
        StartCB = ['From']
        Vertices = []
        for vertex in self.Graph.keys():
            Vertices.append(vertex)
        Vertices.sort()

        for vertex in Vertices:
            StartCB.append(vertex)

        return StartCB

    def EndGenerateVertexList(self):
        EndCB = ['To']
        Vertices = []
        for vertex in self.Graph.keys():
            Vertices.append(vertex)
        Vertices.sort()

        for vertex in Vertices:
            EndCB.append(vertex)
        return EndCB

    def viewEdges(self, target):
        for vertex in self.Graph.keys():  # Search for the target vertex
            if vertex == target:
                for item in self.Graph[vertex]:  # Return all the edge such vertex is connected to
                    print("From", vertex, "to", item[0],
                          "\nTime:", item[1], "hours",
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

    def CalcTime(self, start, end):
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

    def QuickestRoute(self, start, end):
        if self.__contains__(start) & self.__contains__(end):
            # Find path with the Quickest amount of time
            allPaths = self.find_all_paths(start, end)
            res = []
            for path in allPaths:
                pathTime = 0
                for i in range(len(path) - 1):
                    pathTime = pathTime + self.CalcTime(path[i], path[i + 1])
                res.append(pathTime)

            if len(res) != 0:
                TotalTime = min(res)
                QuickestRoutePath = allPaths[res.index(TotalTime)]
                # Cost
                cost = 0
                for i in range(len(QuickestRoutePath) - 1):
                    cost = cost + self.routeCost(QuickestRoutePath[i], QuickestRoutePath[i + 1])
                # Print
                path = str(QuickestRoutePath).replace('[', '').replace(']', '').replace("'", '').replace(',', ' →')

                return "Total time {0} hours. Total cost {1} dollars. \nRoute: {2}. ".format(
                    TotalTime, cost, path)
            else:
                return False
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
                # Time
                TotalTime = 0
                for i in range(len(CheapestRoutePath) - 1):
                    TotalTime = TotalTime + self.CalcTime(CheapestRoutePath[i], CheapestRoutePath[i + 1])
                # Print
                path = str(CheapestRoutePath).replace('[', '').replace(']', '').replace("'", '').replace(',', ' →')

                return "Total time {1} hours. Total cost {0} dollars. \nRoute: {2}".format(
                    TotalCost, TotalTime, path)
            else:
                return False
        else:
            raise Exception("Start and/or end vertex does not exist in the graph")



