from itertools import permutations

def tsp(graph, start):
    cities = list(graph.keys())
    cities.remove(start)

    best_path = None
    best_cost = float("inf")

    for route in permutations(cities):
        current = start
        cost = 0

        for city in route:
            cost += graph[current][city]
            current = city

        cost += graph[current][start]

        if cost < best_cost:
            best_cost = cost
            best_path = [start] + list(route) + [start]

    return best_path, best_cost


graph = {
    "A": {"B": 10, "C": 15, "D": 20},
    "B": {"A": 10, "C": 35, "D": 25},
    "C": {"A": 15, "B": 35, "D": 30},
    "D": {"A": 20, "B": 25, "C": 30}
}

start = "A"

path, cost = tsp(graph, start)

print("Shortest Path:", " -> ".join(path))
print("Minimum Cost:", cost)