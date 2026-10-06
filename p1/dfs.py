graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

visited = set()

def dfs(node):
    if node in visited:
        return

    print(node)
    visited.add(node)

    for neighbor in graph[node]:
        dfs(neighbor)

dfs('A')