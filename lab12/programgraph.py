class Graph:
    def __init__(self):
        self.graph = {}  # dictionary to store adjacency list

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        # Assuming it's an undirected graph
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex} --> {self.graph[vertex]}")
g = Graph()

# Add edges
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")

# Print the graph
g.print_graph()
