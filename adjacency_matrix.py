class AdjacencyMatrixGraph:
    def __init__(self):
        self.vertices = []
        self.matrix = []
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * len(self.vertices))
    
    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        
        from_index = self.vertices.index(from_vertex)
        to_index = self.vertices.index(to_vertex)
        self.matrix[from_index][to_index] = 1
    
    def __str__(self):
        return ",\n".join("  " + str(row) for row in self.matrix)

edges = [("A", "B"), ("B", "C"), ("C", "A"), ("A", "C")]
graph = AdjacencyMatrixGraph()
for from_vertex, to_vertex in edges:
    graph.add_edge(from_vertex, to_vertex)

print(graph)