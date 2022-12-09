inp = open("input.txt").read()

headLoc = [0, 0]
tailLoc = [0, 0]

visited = [[0, 0]]

def isAdjacent(loc1, loc2):
    headAdj = findAdj(loc1)
    if loc2 in headAdj:
        return True
    if loc1 == loc2:
        return True

def findAdj(loc):
    return [[loc[0] + 1, loc[1]], [loc[0] - 1, loc[1]], [loc[0], loc[1] + 1], [loc[0], loc[1] - 1], [loc[0] + 1, loc[1] + 1], [loc[0] - 1, loc[1] - 1], [loc[0] + 1, loc[1] - 1], [loc[0] - 1, loc[1] + 1]]

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 


for line in inp.splitlines():
    direction, distance = line.split(" ")
    distance = int(distance)
    for i in range(distance):
        if direction == "U":
            headLoc[1] += 1
        elif direction == "D":
            headLoc[1] -= 1
        elif direction == "L":
            headLoc[0] -= 1
        elif direction == "R":
            headLoc[0] += 1
        
        if not isAdjacent(headLoc, tailLoc):
            adjToHead = findAdj(headLoc)
            adjToTail = findAdj(tailLoc)
            moveTo = intersection(adjToHead, adjToTail)[0]
            tailLoc = moveTo
            if moveTo not in visited:
                visited.append(moveTo)

print(len(visited))