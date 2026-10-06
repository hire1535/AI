def alpha_beta(node, alpha, beta, maximizing):

    if node not in graph:
        return node

    if maximizing:
        best = float('-inf')

        for child in graph[node]:
            value = alpha_beta(child, alpha, beta, False)

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for child in graph[node]:
            value = alpha_beta(child, alpha, beta, True)

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [2, 1],
    'F': [2, 8],
    'G': [4, 9]
}

answer = alpha_beta('A', float('-inf'), float('inf'), True)

print("Optimal Value:", answer)