import string

inp = open("input.txt").read()


pairs = []
total = 0

for line in inp.splitlines():
    pairs.append(line.split(","))

for pair in pairs:
    elf1, elf2 = [], []

    for i in range(int(pair[0].split("-")[1])-int(pair[0].split("-")[0])+1):
        elf1.append(int(pair[0].split("-")[0])+i)
    for i in range(int(pair[1].split("-")[1])-int(pair[1].split("-")[0])+1):
        elf2.append(int(pair[1].split("-")[0])+i)
    
    flag = False
    if(any(x in elf1 for x in elf2)):
        flag = True
    
    elif(any(x in elf2 for x in elf1)):
        flag = True

    if(flag):
        total += 1
    
print(total)