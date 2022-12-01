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

print(max(elves))