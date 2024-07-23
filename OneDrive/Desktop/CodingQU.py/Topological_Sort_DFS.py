def topological_sort_dfs(graph):
    def dfs(node, visited, stack):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, stack)
        stack.append(node)

    visited = set()
    stack = []

    for node in graph:
        if node not in visited:
            dfs(node, visited, stack)

    return stack[::-1]  # Reverse the stack to get the topological order

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

print(topological_sort_dfs(graph))
