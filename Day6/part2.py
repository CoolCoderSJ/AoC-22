inp = open("input.txt").read()

j = 0
for i in inp:
    marker = []
    fourChars = inp[j:j+14]
    for char in fourChars:
        if char in marker:
            continue
        else:
            marker.append(char)
    if len(marker) == 14:
        print(j+14)
        break
    
    j += 1