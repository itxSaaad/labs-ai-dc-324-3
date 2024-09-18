def minimax(node, depth, isMaximizingPlayer, alpha, beta):
    if depth == 0 or len(node[1]) == 0:
        return node[0]

    if isMaximizingPlayer:
        best_val = float('-inf')
        for child in node[1]:
            value = minimax(child, depth - 1, False, alpha, beta)
            best_val = max(best_val, value)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                break
        return best_val
    else:
        best_val = float('inf')
        for child in node[1]:
            value = minimax(child, depth - 1, True, alpha, beta)
            best_val = min(best_val, value)
            beta = min(beta, best_val)
            if beta <= alpha:
                break
        return best_val

tree = [3,
            [
                [5,
                [
                    [9, [[8, [], []], [6, [], []]]],
                    [6, [], []]
                    ]
                ],
                [2, [[3, [[1, [], []]], [7, [], []]]]]
            ]
        ]

print(minimax(tree, 3, True, float('-inf'), float('inf')))
