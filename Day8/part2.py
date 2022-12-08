inp = open("input.txt").read()

treeMap = []
for line in inp.splitlines():
    a = []
    for char in line:
        a.append(int(char))

    treeMap.append(a)


def score(rowInd, columnInd, treeMap):
    bottom, top, left, right = [], [], [], []
    bottomCoords = range(rowInd+1, len(treeMap))
    bottomCoords = list(bottomCoords)

    topCoords = range(rowInd)
    topCoords = list(topCoords)
    topCoords.reverse()

    rightCoords = range(columnInd+1, len(treeMap[rowInd]))
    rightCoords = list(rightCoords)

    leftCoords = range(columnInd)
    leftCoords = list(leftCoords)
    leftCoords.reverse()

    for i in bottomCoords:
        bottom.append(treeMap[i][columnInd])
        if treeMap[i][columnInd] >= treeMap[rowInd][columnInd]:
            break

    for i in topCoords:
        top.append(treeMap[i][columnInd])
        if treeMap[i][columnInd] >= treeMap[rowInd][columnInd]:
            break

    for i in rightCoords:
        right.append(treeMap[rowInd][i])
        if treeMap[rowInd][i] >= treeMap[rowInd][columnInd]:
            break

    for i in leftCoords:
        left.append(treeMap[rowInd][i])
        if treeMap[rowInd][i] >= treeMap[rowInd][columnInd]:
            break

    finalScore = len(bottom) * len(top) * len(left) * len(right)
    return finalScore


scores = {}
rowInd = 0
for row in treeMap:
    columnInd = 0
    for column in row:
        scenicScore = score(rowInd, columnInd, treeMap)
        scores[(rowInd, columnInd)] = scenicScore
        columnInd += 1
    rowInd += 1

print(max(scores.values()))
