def minimax(node, depth, is_maximizing, graph, values):
    # Terminal condition: reached leaf node or max depth
    if depth == 0 or node not in graph or not graph[node]:
        return values.get(node, 0)

    if is_maximizing:
        best = float('-inf')
        for child in graph[node]:
            val = minimax(child, depth - 1, False, graph, values)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for child in graph[node]:
            val = minimax(child, depth - 1, True, graph, values)
            best = min(best, val)
        return best
# Graph representation of the game tree
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 
    'E': [], 
    'F': [],
}

# Values at leaf nodes (terminal states)
values = {
    'D': 3,
    'E': 1,
    'F': 1
}

# Call Minimax on the root node 'A'
best_value = minimax('A', 3, True, graph, values)
print("Best value for MAX player at root A:", best_value)
