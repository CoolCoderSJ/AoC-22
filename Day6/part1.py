inp = open("input.txt").read()

j = 0
for i in inp:
    marker = []
    fourChars = inp[j:j+4]
    for char in fourChars:
        if char in marker:
            continue
        else:
            marker.append(char)
    if len(marker) == 4:
        print(j+4)
        break
    
    j += 1