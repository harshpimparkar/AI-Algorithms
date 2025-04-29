import heapq

def gbfs(start,goal,heuristic_fn):
    
    visited = set()
    queue=[]
    heapq.heappush(queue,(heuristic_fn[start],start,[start]))
    
    while queue:
        cost , node, path = heapq.heappop(queue)
        print("Visited:",node , "Heuristic Value: ",cost)
        visited.add(node)
        if node == goal:
            print("Goal Reached\nPath: ","->".join(path))
            return
        for neightbor in graph.get(node, []):
            if neightbor not in visited:
                heapq.heappush(queue, (heuristic_fn[neightbor],neightbor,path+[neightbor]))
    print("Unreachable")
    
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": [],
}

heuristic_fn = {
    "A":5,
    "B":4,
    "C":3,
    "D":2,
    "E":1,
    "F":0
}

gbfs('A','F',heuristic_fn)