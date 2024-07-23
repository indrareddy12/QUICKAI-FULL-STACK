def bellman_ford(graph, start):
    # Step 1: Initialize distances from start to all vertices as infinity and start to itself as 0
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Step 2: Relax all edges |V| - 1 times.
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight

    # Step 3: Check for negative-weight cycles.
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                print("Graph contains a negative-weight cycle")
                return None

    return distances

# Example usage:
graph = {
    'A': {'B': 1},
    'B': {'C': 3, 'D': 2},
    'C': {'A': -6},
    'D': {'C': 1}
}

start_vertex = 'A'
distances = bellman_ford(graph, start_vertex)

if distances:
    print(f"Shortest distances from {start_vertex}:")
    for vertex in distances:
        print(f"Distance to {vertex}: {distances[vertex]}")
