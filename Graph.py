class Graph:
    def __init__(self):
        self.Graph = {}

    def addVertex(self, city):
        self.Graph[city] = []

    def addEdge(self, start, end, dist, cost):
        if start not in self.Graph:
          self.addVertex(start)
        if end not in self.Graph:
          self.addVertex(end)
        self.Graph[start] = self.Graph[start] + [[end, dist, cost]]

    def removeEdge(self, start, end,distance,cost):
        for startPoint in self.Graph.keys():
            if startPoint == start:
                for item in self.Graph[startPoint]:
                    if item[0] == end:
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

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
      path = path + [start_vertex]
      if start_vertex == end_vertex:
          return [path]

      # If the start vertex is no in Graph
      vertex = [] 
      for x in self.Graph.keys():
        vertex.append(x)

      if start_vertex not in vertex:
        return []
        

      # If the start verex is in graph
      paths = []
      for vertex in self.Graph[start_vertex]:
          if vertex[0] not in path:
              extended_paths = self.find_all_paths(vertex[0],end_vertex,path)
              for p in extended_paths:
                  paths.append(p)
        
      return paths

    def routeCost(self, start, end):
      totalcost = 0
      for route in self.Graph[start]:
        if route[0] == end:
          totalcost = totalcost + route[2]
      return totalcost
    def distancecost(self, start, end):
      totalcost = 0
      for route in self.Graph[start]:
        if route[0] == end:
          totalcost = totalcost + route[1]
      return totalcost  
      
    def CheapestValue(self, start, end):
      allpath = self.find_all_paths(start, end)
      res = []
      for path in allpath:
        costofpath = 0 
        for i in range(len(path)-1):
          costofpath = costofpath + self.routeCost(path[i],path[i+1])
        res.append(costofpath)
      return allpath[res.index(min(res))], min(res)

      
    def shortestroute(self, start, end):
      allpath = self.find_all_paths(start, end)
      res = []
      for path in allpath:
        costofpath = 0 
        for i in range(len(path)-1):
          costofpath = costofpath + self.distancecost(path[i],path[i+1])
        res.append(costofpath)
      return allpath[res.index(min(res))], min(res)
if __name__ == "__main__":
    a = Graph()
    a.addVertex("China")
    a.addVertex("Russia")
    a.addVertex("US")
    a.addEdge("China", "US", 2000, 150)
    a.addEdge("US", "Russia", 800, 80)
    a.addEdge("China", "meowcity", 800, 80)
    a.addEdge("CatCity", "China", 100000, 100000)
    a.addEdge("US", "DogCity", 10,10)
    a.addEdge("DogCity", "Russia", 10, 20)
    a.TestPrint()
    # print(a.Graph["China"])
    # a.removeEdge("China","US",2000,150)
    # a.TestPrint()
    # print(a.Graph["China"])
    # print(a.Graph["China"])
    print(a.find_all_paths('China','Russia'))
    print(a.CheapestValue('China','Russia'))
    print(a.shortestroute('China','Russia'))
