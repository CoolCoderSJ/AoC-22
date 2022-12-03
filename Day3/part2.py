import string

inp = open("input.txt").read()
data = inp.splitlines()

total = 0

n = 3
groups = [data[i:i+n] for i in range(0, len(data), n)] 

lowercaseLetters = list(string.ascii_lowercase)
uppercaseLetters = list(string.ascii_uppercase)

for group in groups:
    badge = "".join(set(group[0]).intersection(group[1], group[2]))
    if badge in lowercaseLetters:
        priority = lowercaseLetters.index(badge)+1
    elif badge in uppercaseLetters:
        priority = uppercaseLetters.index(badge)+27
    total += priority
    
print(total)