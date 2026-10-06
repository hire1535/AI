import heapq

def calculate_heuristic(graph, goal):
    heuristic = {}
    priority_queue = [(0, goal)]
    visited = set()

    while priority_queue:
        cost, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        heuristic[current] = cost

        for node in graph:
            if current in graph[node] and node not in visited:
                heapq.heappush(priority_queue, (cost + 1, node))

    for node in graph:
        if node not in heuristic:
            heuristic[node] = float("inf")

    return heuristic


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

start = "A"
goal = "G"

heuristic = calculate_heuristic(graph, goal)

path = greedy_best_first_search(graph, heuristic, start, goal)

if path:
    print("Path:", " -> ".join(path))
else:
    print("Path not found")