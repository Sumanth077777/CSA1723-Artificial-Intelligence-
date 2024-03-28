from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited.add(v)

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

# Example usage:
if __name__ == "__main__":
    g = Graph()
    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges (format: source destination):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    start_vertex = int(input("Enter the starting vertex for DFS: "))
    g.dfs(start_vertex)
