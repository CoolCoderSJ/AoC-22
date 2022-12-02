inp = open("input.txt").read()

scoreGuide = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "loss": 0,
    "draw": 3,
    "win": 6
}

scorePair = {
    "A X": "draw",
    "A Y": "win",
    "A Z": "loss",
    "B X": "loss",
    "B Y": "draw",
    "B Z": "win",
    "C X": "win",
    "C Y": "loss",
    "C Z": "draw"
}

score = 0
for line in inp.splitlines():
    line = line.strip()
    splitLine = line.split(" ")
    throw = splitLine[1]
    score += scoreGuide[throw]

    score += scoreGuide[scorePair[line]]

print(score)