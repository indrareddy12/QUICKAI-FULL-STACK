import heapq

def dijkstra(graph, start):
    # Priority queue to hold the vertices to explore and their current distances
    priority_queue = [(0, start)]
    # Dictionary to hold the shortest path to each vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    # Dictionary to hold the shortest path tree
    previous_vertices = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Nodes can get added to the priority queue multiple times. We only process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_vertices

def print_shortest_path(previous_vertices, start, end):
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    path = path[::-1]
    if path[0] == start:
        print("Shortest path: ", " -> ".join(path))
    else:
        print(f"No path from {start} to {end}")

# Example usage
graph = {
    'A': {'B': 7, 'C': 9, 'F': 14},
    'B': {'A': 7, 'C': 10, 'D': 15},
    'C': {'A': 9, 'B': 10, 'D': 11, 'F': 2},
    'D': {'B': 15, 'C': 11, 'E': 6},
    'E': {'D': 6, 'F': 9},
    'F': {'A': 14, 'C': 2, 'E': 9}
}

start_vertex = 'A'
end_vertex = 'E'
distances, previous_vertices = dijkstra(graph, start_vertex)
print(f"Shortest distance from {start_vertex} to {end_vertex} is {distances[end_vertex]}")
print_shortest_path(previous_vertices, start_vertex, end_vertex)
