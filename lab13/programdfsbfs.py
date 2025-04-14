from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)  # for undirected graph

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        print("BFS Traversal:", end=" ")
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()  # for newline

    def dfs(self, vertex, visited=None):
        if visited is None:
            visited = set()
            print("DFS Traversal:", end=" ")
        print(vertex, end=" ")
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def print_graph(self):
        print("\nGraph (Adjacency List):")
        for vertex in self.graph:
            print(f"{vertex} --> {self.graph[vertex]}")
          
# Create the graph
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')

# Print graph structure
g.print_graph()

# Run BFS and DFS
g.bfs('A')
g.dfs('A')
