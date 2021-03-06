# Your task is to complete this function
# Function should print DFS Traversal
# Graph(graph) is a defaultict of type List
# Starting vertex (s) is 1
# Need not print new Line
# n is no of edges
# visit is a boolean array initialized to False
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def DFSUtil(self, v, visited):
    
        visited[v] =  True
        print(v, end=' ')
        
        for vertex in self.graph[v]:
            if (not(visited[vertex])):
                visited[vertex] = True
                self.DFSUtil(vertex, visited)

    def DFS(self):
        V = len(self.graph)
        visited = [False] * (V + 1)
        for i in self.graph:
            if (not(visited[i])):
                self.DFSUtil(i, visited)


def mount_graph(edges, graph):
    for i in range(0, len(edges), 2):
        graph.addEdge(edges[i], edges[i + 1])

tests = int(input())

for i in range(tests):
    g = Graph()
    total_edges = int(input())
    edges = [int(x) for x in input().split()]
    mount_graph(edges, g)
    
    g.DFS()




