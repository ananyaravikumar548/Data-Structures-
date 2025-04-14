class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def is_cyclic_util(self, vertex, visited, rec_stack):
        visited.add(vertex)
        rec_stack.add(vertex)

        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(vertex)
        return False

    def has_cycle(self):
        visited = set()
        rec_stack = set()

        for vertex in self.graph:
            if vertex not in visited:
                if self.is_cyclic_util(vertex, visited, rec_stack):
                    return True
        return False
g = DirectedGraph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'A')  # Cycle exists

if g.has_cycle():
    print("Cycle Detected (Directed)")
else:
    print("No Cycle (Directed)")
