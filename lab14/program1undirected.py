class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Undirected

    def is_cyclic_util(self, vertex, visited, parent):
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                if self.is_cyclic_util(neighbor, visited, vertex):
                    return True
            elif neighbor != parent:
                return True
        return False

    def has_cycle(self):
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                if self.is_cyclic_util(vertex, visited, None):
                    return True
        return False
g = Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'A')  # Cycle exists

if g.has_cycle():
    print("Cycle Detected (Undirected)")
else:
    print("No Cycle (Undirected)")
