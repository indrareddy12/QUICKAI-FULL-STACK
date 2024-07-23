import heapq

def prim(graph, start):
    # Priority queue to store the edges along with their weights
    pq = []
    heapq.heappush(pq, (0, start))
    total_cost = 0
    visited = set()
    mst_edges = []

    while pq:
        weight, current_vertex = heapq.heappop(pq)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)
        total_cost += weight

        # Add the edge to the MST (excluding the first dummy edge with weight 0)
        if weight != 0:
            mst_edges.append((prev_vertex, current_vertex, weight))

        for neighbor, edge_weight in graph[current_vertex].items():
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor))
                prev_vertex = current_vertex

    return mst_edges, total_cost

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
mst_edges, total_cost = prim(graph, start_vertex)

print("Minimum Spanning Tree edges:")
for edge in mst_edges:
    print(edge)

print(f"Total cost: {total_cost}")
