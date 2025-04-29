def hill_climbing(graph, heuristic, start, goal):
    current = start
    path = [current]

    while current != goal:
        neighbors = graph.get(current, [])
        if not neighbors:
            print(f"No neighbors to move from {current}.")
            return None

        # Pick the neighbor with the lowest heuristic value
        best = min(neighbors, key=lambda n: heuristic.get(n, float('inf')))
        
        # Stop if no improvement
        if heuristic[best] >= heuristic[current]:
            print(f"Stuck at local minimum: {current}")
            return None

        current = best
        path.append(current)

    return path

graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H', 'X'],
    'D': [],
    'E': [],
    'F': ['I'],
    'G': ['J'],
    'H': [],
    'I': ['K'],
    'J': ['K'],
    'K': [],
    'X': []
}

heuristic = {
    'S': 100,
    'A': 85,
    'B': 78,
    'C': 41,
    'D': 39,
    'E': 32,
    'F': 21,
    'G': 17,
    'H': 12,
    'I': 15, 
    'J': 10,
    'K': 5,
    'X': 1 
}

start_node = 'S'
goal_node = 'K'

result = hill_climbing(graph, heuristic, start_node, goal_node)
if result:
    print("Path found:", " -> ".join(result))
else:
    print("Goal not found.")
