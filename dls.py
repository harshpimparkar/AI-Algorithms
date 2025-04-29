graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": [],
}

def dls(start, goal, path, level, maxDepth):
    print("Current level:", level, "Node:", start)
    path.append(start)
    if start == goal:
        return path
    if level == maxDepth:
        path.pop()
        return False
    for child in graph[start]:
        if dls(child, goal, path, level + 1, maxDepth):
            return path
    path.pop()
    return False

start = 'A'
goal = input('Enter target: ')
maxDepth = int(input('Enter maximum depth: '))
path = []
result = dls(start, goal, path, 0, maxDepth)
if result:
    print("DLS Path:", " -> ".join(path))
else:
    print("Path to goal node not found for given max depth.")
