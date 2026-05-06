from collections import deque

graph = {
    0:[1,2],
    1:[2],
    2:[0,3],
    3:[3]
}

# BFS
def bfs(start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

# DFS
def dfs(node, visited=set()):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

print("BFS:")
bfs(0)

print("\nDFS:")
dfs(0)
