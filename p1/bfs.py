from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

visited = set()
queue = deque()

queue.append('A')

def bfs():
    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        print(node)

        for neighbor in graph[node]:
            queue.append(neighbor)

bfs()