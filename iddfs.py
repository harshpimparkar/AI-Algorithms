graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": [],
}

def iddfs(start,goal,path,level):
    print("Level: ",level)
    path.append(start)
    if start ==  goal:
        return path
    for child in graph[start]:
        if iddfs(child,goal,path,level+1):
            return path
    path.pop()
    return False

start = 'A'
goal = input('Enter target: ')
# maxDepth = int(input('Enter maximum depth: '))
path = []
result = iddfs(start, goal, path, 0)
if result:
    print("DLS Path:", " -> ".join(path))
else:
    print("Path to goal node not found for given max depth.")



