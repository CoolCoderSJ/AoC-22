inp = open("input.txt").read()

scoreGuide = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3,
    "loss": 0,
    "draw": 3,
    "win": 6
}

secondColumn = {
    "X": "loss",
    "Y": "draw",
    "Z": "win"
}

score = 0
for line in inp.splitlines():
    line = line.strip()
    splitLine = line.split(" ")
    them = splitLine[0]
    end = splitLine[1]
    
    score += scoreGuide[secondColumn[end]]

    if end == "X" and them == "A":
        score += scoreGuide["Z"]
    elif end == "X" and them == "B":
        score += scoreGuide["X"]
    elif end == "X" and them == "C":
        score += scoreGuide["Y"]
    elif end == "Y":
        score += scoreGuide[them]
    elif end == "Z" and them == "A":
        score += scoreGuide["Y"]
    elif end == "Z" and them == "B":
        score += scoreGuide["Z"]
    elif end == "Z" and them == "C":
        score += scoreGuide["X"]
    

print(score)