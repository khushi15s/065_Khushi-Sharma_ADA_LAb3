# Adjacency List
graph = {
    0: [1,2],
    1: [2],
    2: [0,3],
    3: [3]
}

print("Adjacency List:", graph)

# Adjacency Matrix
matrix = [
    [0,1,1,0],
    [0,0,1,0],
    [1,0,0,1],
    [0,0,0,1]
]

print("Adjacency Matrix:")
for row in matrix:
    print(row)