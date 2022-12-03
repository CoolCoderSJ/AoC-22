import string

inp = open("input.txt").read()

total = 0

for line in inp.splitlines():
    rucksack = line.strip()
    firstpart, secondpart = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    commonItem = ''.join(set(firstpart).intersection(secondpart))

    lowercaseLetters = list(string.ascii_lowercase)
    uppercaseLetters = list(string.ascii_uppercase)

    if commonItem in lowercaseLetters:
        priority = lowercaseLetters.index(commonItem)+1
    
    elif commonItem in uppercaseLetters:
        priority = uppercaseLetters.index(commonItem)+27
    
    total += priority

print(total)