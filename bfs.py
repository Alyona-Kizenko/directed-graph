from collections import deque

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
        return "\n".join(f"{vertex}: {neighbors}" for vertex, neighbors in self.adjacency_list.items())

def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)
    result = []
    
    while queue:
        current_vertex = queue.popleft()
        result.append(current_vertex)
        
        for neighbor in graph.adjacency_list.get(current_vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

dg = DirectedGraph()
dg.add_vertex("A")
dg.add_vertex("B")
dg.add_vertex("C")
dg.add_vertex("D")
dg.add_edge("A", "B")
dg.add_edge("A", "C")
dg.add_edge("B", "D")
dg.add_edge("C", "A")
dg.add_edge("D", "C")

print(dg)

print(bfs(dg, "A"))
print(bfs(dg, "C"))