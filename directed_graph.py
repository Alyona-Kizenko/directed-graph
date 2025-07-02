class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.adjacency_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.adjacency_list:
            self.add_vertex(to_vertex)
        self.adjacency_list[from_vertex].append(to_vertex)
    
    def __str__(self):
        return "\n".join(f"{vertex}: {neighbors}"for vertex, neighbors in self.adjacency_list.items())


dg = DirectedGraph()
dg.add_vertex("A")
dg.add_vertex("B")
dg.add_vertex("C")
dg.add_edge("A", "B")
dg.add_edge("B", "C")
dg.add_edge("C", "A")
dg.add_edge("A", "C")

print(dg)
