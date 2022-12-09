inp = open("input.txt").read()

headLoc = [0, 0]
midLocs = {
    "loc1": [0, 0],
    "loc2": [0, 0],
    "loc3": [0, 0],
    "loc4": [0, 0],
    "loc5": [0, 0],
    "loc6": [0, 0],
    "loc7": [0, 0],
    "loc8": [0, 0],
}
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
        
        if not isAdjacent(headLoc, midLocs['loc1']):
            adjToHead = findAdj(headLoc)
            adjToLoc1 = findAdj(midLocs['loc1'])
            moveTo = intersection(adjToHead, adjToLoc1)[0]
            midLocs['loc1'] = moveTo
        
        for i in range(7):
            if not isAdjacent(midLocs[f'loc{i+1}'], midLocs[f'loc{i+2}']):
                adjToPrev = findAdj(midLocs[f'loc{i+1}'])
                adjToLoc = findAdj(midLocs[f'loc{i+2}'])
                moveTo = intersection(adjToPrev, adjToLoc)[0]
                midLocs[f'loc{i+2}'] = moveTo

        if not isAdjacent(midLocs['loc8'], tailLoc):
            adjToLoc8 = findAdj(midLocs['loc8'])
            adjToTail = findAdj(tailLoc)
            moveTo = intersection(adjToLoc8, adjToTail)[0]
            tailLoc = moveTo
            if moveTo not in visited:
                visited.append(moveTo)

print(len(visited))