from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node,end="")
            visited.add(node)
            queue.extend(graph[node])

graph = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["F","G"],
    "D":["H"],
    "E":[],
    "F":[],
    "G":[],
    "H":[]
}
print("BFS traversal")
bfs(graph,'A')
        
    