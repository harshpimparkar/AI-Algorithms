from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
            result.append(node)
    return result

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for child in graph[start]:
        if child not in visited:
            result.extend(dfs(graph, child, visited))
    return result



graph = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["F"],
    "D":[],
    "E":[],
    "F":[],
}

start = 'A'

print("BFS:" , "->".join(bfs(graph,start)))
print("DFS:" , "->".join(dfs(graph,start)))