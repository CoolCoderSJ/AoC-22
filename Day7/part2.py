import json

inp = open("input.txt").read()


sizes = {

}

currentPath = ""

k = 0
for line in inp.splitlines():
    for char in line:
        k += 1

    if line.startswith("$ "):
        cmd = line[2:]
        if cmd.startswith("cd"):
            path = cmd[3:]
            if path == "..":
                currentPath = currentPath[:currentPath.rfind("[")]
            elif path == "/":
                currentPath = "['/']"
            else:
                currentPath += "['" + path + "']"

            if currentPath == "":
                currentPath = "['/']"
            
            currentPath = currentPath.replace("//", "/")

        elif cmd == "ls":
            files = inp[k:].split("$")[0].strip()
            for f in files.splitlines():
                if f.startswith("dir "):
                    continue
                else:
                    size, filename = f.split(" ")
                    
                    for p in currentPath.split("['")[1:]:
                        p = p[:-2]
                        if p not in sizes:
                            sizes[p] = 0
                        sizes[p] += int(size)
                        
    k += 1

total = 0
for k, v in sizes.items():
    if k != "/" and v <= 100000:
        total += v

print(total)

