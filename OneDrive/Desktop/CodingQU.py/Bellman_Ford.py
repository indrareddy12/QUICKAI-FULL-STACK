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
    'A': {'B': 7, 'C': 9, 'F': 14},
    'B': {'A': 7, 'C': 10, 'D': 15},
    'C': {'A': 9, 'B': 10, 'D': 11, 'F': 2},
    'D': {'B': 15, 'C': 11, 'E': 6},
    'E': {'D': 6, 'F': 9},
    'F': {'A': 14, 'C': 2, 'E': 9}
}

start_vertex = 'A'
distances = bellman_ford(graph, start_vertex)

if distances:
    print(f"Shortest distances from {start_vertex}:")
    for vertex in distances:
        print(f"Distance to {vertex}: {distances[vertex]}")
