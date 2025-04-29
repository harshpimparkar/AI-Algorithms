import heapq

def ucs(graph,start,goal):
    
    queue = [(0,start,[start])]
    visited = set()
    
    while queue:
        cost,node, path = heapq.heappop(queue)
        # if node in visited:
        #     continue
        visited.add(node)
        print("Visited: ",node, "Cost: ",cost)
        if node == goal:
            print("Goal Found!")
            print("Path: ","->".join(path),end="\n")
            print("Cost: ",cost)
            return
        
        for neighbor,edge_cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue,(cost+edge_cost,neighbor,path+[neighbor]))
                
    print("Goal Unreachable!")
    
graph={
    "A": [("B",2),("C",5)],
    "B": [("D",9)],
    "C":[],
    "D":[]
}

start = 'A'
goal = 'C'
ucs(graph,start,goal)
    