inp = open("input.txt").read()

coords = []
start, end = None, None

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

i = 0
for line in inp.splitlines():
    j = 0
    for char in line:
        if char == "S":
            coords.append({
                "coords": (i, j),
                "level": 0
            })
            start = {
                "coords": (i, j),
                "level": 0
            }
        elif char == "E":
            coords.append({
                "coords": (i, j),
                "level": 25
            })
            end = {
                "coords": (i, j),
                "level": 25
            }
        else:
            coords.append({
                "coords": (i, j),
                "level": letters.index(char)
            })
        j += 1
    i += 1

def get_neighbors(coords, coord, level):
    neighbors = []
    for c in coords:
        if (c["coords"] == (coord[0] + 1, coord[1]) or c["coords"] == (coord[0] - 1, coord[1]) or c["coords"] == (coord[0], coord[1] + 1) or c["coords"] == (coord[0], coord[1] - 1)) and c['level'] <= level+1:
            neighbors.append(c)
    return neighbors

def get_path(coords, start, end):
    global distances
    path = [{
        "coords": start,
        "level": 0
    }]
    distances = {start['coords']: 0}
    current = [start]
    while end['coords'] not in distances:
        for c in current:
            neighbors = get_neighbors(coords, c['coords'], c['level'])
            for n in neighbors:
                if n['coords'] not in [p['coords'] for p in path]:
                    path.append(n)
                    current.append(n)
                    distances[n['coords']] = distances[c['coords']] + 1
    return path

get_path(coords, start, end)
print(distances[end['coords']])