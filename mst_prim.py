import heapq

graph = {
    0: [(2,1),(6,3)],
    1: [(2,0),(3,2),(8,3),(5,4)],
    2: [(3,1),(7,4)],
    3: [(6,0),(8,1)],
    4: [(5,1),(7,2)]
}

def prim(start):
    visited = set()
    min_heap = [(0, start)]  # (weight, node)
    total_cost = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node not in visited:
            visited.add(node)
            total_cost += weight

            for w, neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor))

    return total_cost

print("Minimum Cost of MST:", prim(0))
