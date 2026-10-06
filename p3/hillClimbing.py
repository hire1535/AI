def hill_climbing(values):
    current = 0

    while True:
        left = current - 1
        right = current + 1

        best = current

        if left >= 0 and values[left] > values[best]:
            best = left

        if right < len(values) and values[right] > values[best]:
            best = right

        if best == current:
            break

        current = best

    return values[current]


values = [1, 5, 3, 8, 6, 10, 7]

result = hill_climbing(values)

print("Maximum value:", result)