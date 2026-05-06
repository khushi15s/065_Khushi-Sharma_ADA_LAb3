def bellman_ford(edges, V, source):
    dist = [float('inf')] * V
    dist[source] = 0
    
    for _ in range(V-1):
        for u,v,w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    return dist

edges = [
    (0,1,4), (0,2,1), (2,1,2),
    (1,3,1), (2,3,5)
]

print("Distances:", bellman_ford(edges, 4, 0))
