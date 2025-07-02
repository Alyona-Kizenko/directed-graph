def create_adjacency_list(edges):
    graph = {}
    for from_vertex, to_vertex in edges:
        if from_vertex not in graph:
            graph[from_vertex] = []
        if to_vertex not in graph:
            graph[to_vertex] = []
        graph[from_vertex].append(to_vertex)
    return graph


def add_vertex_to_adj_list(adj_list, vertex):
    if vertex not in adj_list:
        adj_list[vertex] = []


def add_edge_to_adj_list(adj_list, from_vertex, to_vertex):
    add_vertex_to_adj_list(adj_list, from_vertex)
    add_vertex_to_adj_list(adj_list, to_vertex)
    adj_list[from_vertex].append(to_vertex)


edges = [("A", "B"), ("B", "C"), ("C", "A"), ("A", "C")]
adj_list = create_adjacency_list(edges)
print(adj_list)

add_vertex_to_adj_list(adj_list, "D")
add_edge_to_adj_list(adj_list, "C", "D")
print(adj_list)