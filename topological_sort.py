from collections import defaultdict

graph = defaultdict(list)

graph[5].append(2)
graph[5].append(0)
graph[4].append(0)
graph[4].append(1)
graph[2].append(3)
graph[3].append(1)

visited = set()
stack = []

def dfs(v):
    visited.add(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor)
    stack.append(v)

for i in range(6):
    if i not in visited:
        dfs(i)

print("Topological Sort:", stack[::-1])
