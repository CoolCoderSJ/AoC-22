inp = open("input.txt").read()

register = 1
cycle = 0

intervals = []

for line in inp.splitlines():
    if line.startswith("addx"):
        amt = int(line.split(" ")[1])
        cycleInc = 2
    else:
        amt = 0
        cycleInc = 1
    
    for i in range(cycleInc):
        cycle += 1
        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            intervals.append(register*cycle)
        if cycleInc == 2 and i != 0:
            register += amt
        elif cycleInc == 1:
            register += amt

print(sum(intervals))