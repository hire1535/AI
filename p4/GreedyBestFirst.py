import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], start)]
    visited = set()
    parent = {start: None}

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor)
                )

    return None


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": ["G"],
    "G": []
}

heuristic = {
    "A": 7,
    "B": 6,
    "C": 4,
    "D": 5,
    "E": 2,
    "F": 3,
    "G": 0
}

start = "A"
goal = "G"

path = greedy_best_first_search(graph, heuristic, start, goal)

if path:
    print("Path:", " -> ".join(path))
else:
    print("Path not found")