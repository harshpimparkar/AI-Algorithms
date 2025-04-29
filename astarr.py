import heapq

def a_star(graph, start, goal, heuristic):
    
    queue = [(heuristic[start], 0, start, [start])]  # (estimated_total_cost, cost_so_far, current_node, path)
    visited = set()

    while queue:
        est_total_cost, cost, current_node, path = heapq.heappop(queue)

        if current_node == goal:
            print("Reached", goal, "with total cost:", cost)
            print("Path:", " -> ".join(path))
            return

        visited.add(current_node)

        for neighbor, edge_cost in graph.get(current_node, []):
            if neighbor not in visited:
                new_cost = cost + edge_cost
                estimated_cost = new_cost + heuristic[neighbor]
                heapq.heappush(queue, (estimated_cost, new_cost, neighbor, path + [neighbor]))

    print("Goal not reachable.")

# Graph and heuristic function
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 5)],
    'D': []
}

heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}

a_star(graph, 'A', 'D', heuristic)
