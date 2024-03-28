from collections import deque

def bfs(graph, start, target):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        if node == target:
            return path 

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))  

    return None
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_node = 'A'
target_node = 'F'
path_to_target = bfs(graph, start_node, target_node)

if path_to_target:
    print(f"Path from {start_node} to {target_node}: {' -> '.join(path_to_target)}")
else:
    print(f"Target node {target_node} not found from node {start_node}")
