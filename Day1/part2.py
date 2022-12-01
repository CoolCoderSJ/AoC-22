inp = open("input.txt").read()

elves = []

num = 0
for line in inp.splitlines():
    line = line.strip()
    if line == "":
        elves.append(num)
        num = 0
    else:
        num += int(line)

total = 0

for i in range(3):
    maxVal = max(elves)
    elves.remove(maxVal)
    total += maxVal

print(total)