def minimax(node, depth, is_max_player):
    if depth == 0 or len(node[1]) == 0:
        return node[0]

    if is_max_player:
        max_val = float('-inf')
        for child in node[1]:
            val = minimax(child, depth - 1, False)
            max_val = max(max_val, val)
        return max_val
    else:
        min_val = float('inf')
        for child in node[1]:
            val = minimax(child, depth - 1, True)
            min_val = min(min_val, val)
        return min_val

tree = [3, [
             [5, [
                  [9, [
                       [8, [], []],
                       [6, [], []]
                      ]],
                  [6, [], []]
                 ]],
             [2, [
                  [3, [
                       [1, [], []],
                       [7, [], []]
                      ]]
                 ]]
           ]]

print(minimax(tree, 3, True))
