import heapq

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

heuristic = {
    "A": 7,
    "B": 6,
    "C": 4,
    "D": 3,
    "E": 0
}

start = "A"
goal = "E"

path, cost = a_star(graph, heuristic, start, goal)

if path:
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("Path not found")