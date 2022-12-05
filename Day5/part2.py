import pprint 
out = pprint.PrettyPrinter(width=72, compact=True)

inp = open("input.txt").read()

crates = {}

crateInput = inp.split("\n\n")[0].split("\n")[:-1]
chunks = []

for line in crateInput:
    line += " "
    n = 4
    chunkList = [line[i:i+n] for i in range(0, len(line), n)]
    chunkList = [x.strip().replace("[", "").replace("]", "") for x in chunkList]
    chunks.append(chunkList)

chunks.reverse()

k = 1
for j in range(len(chunks[0])):
    if chunks[0][j] != " ":
        crates[k] = []
        k += 1

for chunk in chunks:
    i = 1
    chunk = [x for x in chunk if x != " "]
    for c in chunk:
        if c != " " and c != "":
            crates[i].append(c)
        i += 1

instructions = inp.split("\n\n")[1].split("\n")

for inst in instructions:
    amt = int(inst.split(" ")[1])*-1
    fromCrate = int(inst.split(" ")[3])
    toCrate = int(inst.split(" ")[5])

    supplies = crates[fromCrate][amt:]
    del crates[fromCrate][amt:]
    for supply in supplies:
        crates[toCrate].append(supply)

result = ""

for crate, value in crates.items():
    result += value[-1]

print(result)