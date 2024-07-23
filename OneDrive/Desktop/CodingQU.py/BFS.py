from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the starting node

    while queue:
        vertex = queue.popleft()  # Dequeue a node from the front of the queue
        if vertex not in visited:
            visited.add(vertex)  # Mark the node as visited
            print(vertex)  # Process the node
            # Enqueue all unvisited neighbors
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
bfs(graph, 'A')
