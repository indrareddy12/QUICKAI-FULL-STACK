def dfs_cycle(graph, node, visited, parent):
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs_cycle(graph, neighbor, visited, node):
                return True
        elif neighbor != parent:
            return True

    return False

def has_cycle(graph):
    visited = {node: False for node in graph}

    for node in graph:
        if not visited[node]:
            if dfs_cycle(graph, node, visited, None):
                return True

    return False

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
    'E': ['F'],
    'F': ['E']
}

print("Graph has a cycle" if has_cycle(graph) else "Graph does not have a cycle")


#I apologize for the confusion. The condition if visited[neighbor] and neighbor != parent can be misunderstood because I didn't explicitly write if visited[neighbor] as you mentioned. Instead, I'm using neighbor not in visited, which serves a similar purpose in this context. However, to be clear, I'll rewrite the code with explicit boolean checks and make it clearer for understanding.