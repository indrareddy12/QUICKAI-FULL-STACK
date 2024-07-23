from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridge_util(self, u, visited, parent, low, disc, bridges):
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                self.bridge_util(v, visited, parent, low, disc, bridges)
                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def find_bridges(self):
        visited = [False] * self.V
        disc = [float("Inf")] * self.V
        low = [float("Inf")] * self.V
        parent = [-1] * self.V
        bridges = []

        for i in range(self.V):
            if not visited[i]:
                self.bridge_util(i, visited, parent, low, disc, bridges)

        return bridges

# Example usage:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)

print("Bridges in the graph:")
bridges = g.find_bridges()
for u, v in bridges:
    print(f"{u} - {v}")
