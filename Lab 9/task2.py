def minimax(node, depth, maximizingPlayer):
    if depth == 0 or len(node[1]) == 0:
        return node[0]
    if maximizingPlayer:
        max_eva = float('-inf')
        for child in node[1]:
            eva = minimax(child, depth - 1, False)
            max_eva = max(max_eva, eva)
        return max_eva
    else:
        min_eva = float('inf')
        for child in node[1]:
            eva = minimax(child, depth - 1, True)
            min_eva = min(min_eva, eva)
        return min_eva

tree = [3, [[5, [[9, [[8, [], []], [6, [], []]]], [6, [], []]], [2, [[3, [[1, [], []]], [7, [], []]]]]]]]

print(minimax(tree, 3, True))
