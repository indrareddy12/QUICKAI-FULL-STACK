from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def _ap_util(self, u, visited, ap, parent, low, disc):
        children = 0
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                self._ap_util(v, visited, ap, parent, low, disc)

                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    ap[u] = True

                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def find_ap(self):
        visited = [False] * self.V
        disc = [float('Inf')] * self.V
        low = [float('Inf')] * self.V
        parent = [-1] * self.V
        ap = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                self._ap_util(i, visited, ap, parent, low, disc)

        for index, value in enumerate(ap):
            if value:
                print(index)

# Example usage:             #    
   #    0
#/ \
 # 1---2
 #  |
  # 3
  # |
  # 4

   
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

print("Articulation points in the graph:")
g.find_ap()
