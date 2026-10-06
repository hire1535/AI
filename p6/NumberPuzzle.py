from collections import deque

def solve_puzzle(start, goal):
    size = int(len(start) ** 0.5)

    if size * size != len(start):
        print("Invalid puzzle size")
        return None

    if len(start) != len(goal):
        print("Start and goal must have same size")
        return None

    queue = deque([(start, [], [])])
    visited = {tuple(start)}

    while queue:
        state, path, moves = queue.popleft()

        if state == goal:
            return path + [state], moves

        zero = state.index(0)
        row = zero // size
        col = zero % size

        possible_moves = []

        if row > 0:
            possible_moves.append((zero - size, "UP"))

        if row < size - 1:
            possible_moves.append((zero + size, "DOWN"))

        if col > 0:
            possible_moves.append((zero - 1, "LEFT"))

        if col < size - 1:
            possible_moves.append((zero + 1, "RIGHT"))

        for new_zero, move in possible_moves:
            new_state = state.copy()

            new_state[zero], new_state[new_zero] = (
                new_state[new_zero],
                new_state[zero]
            )

            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                queue.append(
                    (new_state, path + [state], moves + [move])
                )

    return None


start = [
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
]

goal = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
]

result = solve_puzzle(start, goal)

if result:
    solution, moves = result
    size = int(len(start) ** 0.5)

    print("Solution Found")
    print("Total Steps:", len(moves))
    print()

    print("Initial State:")
    for i in range(0, len(solution[0]), size):
        print(solution[0][i:i + size])

    print()

    for i in range(len(moves)):
        print("Step", i + 1, ":", moves[i])

        for j in range(0, len(solution[i + 1]), size):
            print(solution[i + 1][j:j + size])

        print()

else:
    print("No solution found")