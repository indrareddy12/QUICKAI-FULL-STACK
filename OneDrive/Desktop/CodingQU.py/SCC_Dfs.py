from collections import defaultdict

# Step 1: Perform DFS and store nodes in stack by finishing times
def fill_order(graph, v, visited, stack):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            fill_order(graph, neighbor, visited, stack)
    stack.append(v)

# Step 2: Transpose the graph
def transpose_graph(graph):
    transposed_graph = defaultdict(list)
    for v in graph:
        for neighbor in graph[v]:
            transposed_graph[neighbor].append(v)   #For vertex 'A' with neighbor 'B': 
                                                   #transposed_graph['B'].append('A')
                                                   #similarly for all


    return transposed_graph

# Step 3: Perform DFS on the transposed graph
def dfs_on_transposed(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs_on_transposed(graph, neighbor, visited)

# Kosaraju's Algorithm to find and print all SCCs
def kosaraju(graph):
    stack = []
    visited = {v: False for v in graph}

    # Step 1: Fill vertices in stack according to their finishing times
    for v in graph:
        if not visited[v]:
            fill_order(graph, v, visited, stack)

    # Step 2: Create a transposed graph
    transposed_graph = transpose_graph(graph)

    # Step 3: Perform DFS on transposed graph in the order defined by the stack
    visited = {v: False for v in graph}
    while stack:
        v = stack.pop()
        if not visited[v]:
            print("SCC:", end=' ')
            dfs_on_transposed(transposed_graph, v, visited)
            print()

# Example usage
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A', 'D'],
    'D': ['E'],
    'E': ['F', 'H'],
    'F': ['G'],
    'G': ['E'],
    'H': ['I'],
    'I': ['J'],
    'J': ['H']
}

kosaraju(graph)
