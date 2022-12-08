inp = open("input.txt").read()

treeMap = []
for line in inp.splitlines():
    a = []
    for char in line:
        a.append(int(char))

    treeMap.append(a)

visible = 0

def isVisible(rowInd, columnInd, treeMap):
    bottom, top, left, right = [], [], [], []
    for i in range(rowInd+1, len(treeMap)):
        if treeMap[i][columnInd] < treeMap[rowInd][columnInd]:
            bottom.append(treeMap[i][columnInd])

    for i in range(rowInd):
        if treeMap[i][columnInd] < treeMap[rowInd][columnInd]:
            top.append(treeMap[i][columnInd])
    
    for i in range(columnInd+1, len(treeMap[rowInd])):
        if treeMap[rowInd][i] < treeMap[rowInd][columnInd]:
            right.append(treeMap[rowInd][i])
        
    for i in range(columnInd):
        if treeMap[rowInd][i] < treeMap[rowInd][columnInd]:
            left.append(treeMap[rowInd][i])
    
    if len(bottom) == (len(treeMap)-(rowInd+1)) or len(top) == rowInd or len(left) == columnInd or len(right) == (len(treeMap[rowInd])-(columnInd+1)):
        return True

rowInd = 0
for row in treeMap:
    columnInd = 0
    for column in row:
        if rowInd == 0 or rowInd == len(treeMap) - 1 or columnInd == 0 or columnInd == len(row) - 1:
            visible += 1
        elif isVisible(rowInd, columnInd, treeMap):
            visible += 1
        columnInd += 1
    rowInd += 1

print(visible)