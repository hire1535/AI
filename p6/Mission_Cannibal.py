from collections import deque


def valid(missionaries, cannibals):

    if missionaries < 0 or cannibals < 0:
        return False

    if missionaries > 3 or cannibals > 3:
        return False

    if missionaries > 0 and missionaries < cannibals:
        return False

    right_missionaries = 3 - missionaries
    right_cannibals = 3 - cannibals

    if right_missionaries > 0 and right_missionaries < right_cannibals:
        return False

    return True


def solve():

    queue = deque([(3, 3, 0, [])])
    visited = set()

    moves = [
        (1, 0, "1 Missionary"),
        (2, 0, "2 Missionaries"),
        (0, 1, "1 Cannibal"),
        (0, 2, "2 Cannibals"),
        (1, 1, "1 Missionary and 1 Cannibal")
    ]

    while queue:

        missionaries, cannibals, boat, path = queue.popleft()

        if (missionaries, cannibals, boat) in visited:
            continue

        visited.add((missionaries, cannibals, boat))

        if missionaries == 0 and cannibals == 0:
            print("Solution:")
            print(*path, sep="\n")
            return

        for move_missionaries, move_cannibals, move_name in moves:

            if boat == 0:
                new_missionaries = missionaries - move_missionaries
                new_cannibals = cannibals - move_cannibals
                new_boat = 1
                direction = "Left to Right"

            else:
                new_missionaries = missionaries + move_missionaries
                new_cannibals = cannibals + move_cannibals
                new_boat = 0
                direction = "Right to Left"

            if valid(new_missionaries, new_cannibals):
                queue.append((
                    new_missionaries,
                    new_cannibals,
                    new_boat,
                    path + [move_name + " -> " + direction]
                ))


solve()