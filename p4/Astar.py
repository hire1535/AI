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

        for neighbor, edge_cost in graph[current]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (cost + edge_cost, neighbor)
                )

    return heuristic


def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    cost_so_far = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path, cost_so_far[goal]

        for neighbor, cost in graph[current]:
            new_cost = cost_so_far[current] + cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost

                priority = new_cost + heuristic[neighbor]

                heapq.heappush(open_list, (priority, neighbor))

                came_from[neighbor] = current

    return None, float("inf")


graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1), ("E", 3)],
    "E": [("D", 3)]
}

start = "A"
goal = "E"

heuristic = calculate_heuristic(graph, goal)

path, cost = a_star(graph, heuristic, start, goal)

if path:
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("Path not found")