from collections import deque

# Search graph horizontally
def BFS(graph, node):
    visited = set()
    queue = []
    visited.add(node)
    queue.append(node)

    while queue:
        elem = queue.pop(0)

        for n in graph[elem]:
            if n not in visited:
                visited.add(n)
                queue.append(n)

# Search graph vertically
def DFS(graph, node):
    visited = set()
    stack = []

    visited.add(node)
    stack.append(node)

    while stack:
        s = stack.pop()

        for n in reversed(graph[s]):
            if n not in visited:
                visited.add(n)
                stack.append(n)