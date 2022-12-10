inp = open("input.txt").read()

register = 1
cycle = 0

grid = [[], [], [], [], [], []]
spriteLoc = [[0, 0], [0, 1], [0, 2]]

for line in inp.splitlines():
    if line.startswith("addx"):
        amt = int(line.split(" ")[1])
        cycleInc = 2
    else:
        amt = 0
        cycleInc = 1
    
    for i in range(cycleInc):
        cycle += 1
        spriteWrite = list(divmod(cycle-1, 40))
        if spriteWrite in spriteLoc:
            grid[spriteWrite[0]].append("#")
        else:
            grid[spriteWrite[0]].append(" ")

        if cycleInc == 2 and i != 0:
            register += amt
            for j in range(len(spriteLoc)):
                spriteLoc[j][0] = (cycle-1)//40
                spriteLoc[j][1] += amt
        elif cycleInc == 1:
            register += amt
            for j in range(len(spriteLoc)):
                spriteLoc[j][0] = (cycle-1)//40
                spriteLoc[j][1] += amt

for i in grid:
    for j in i:
        print(j, end="")
    print()