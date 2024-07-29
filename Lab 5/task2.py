from collections import deque

def breadth_first_search(graph, start, target):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        if node == target:
            print("\nFound target")
            return

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    print("\nTarget not found")
    return

graph = {
    'A': ['B', 'C', 'D'],
    'B': [ 'E', 'F'],
    'C': ['G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

breadth_first_search(graph, 'A', 'E')
