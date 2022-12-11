from functools import reduce
import json
from operator import mul
inp = open("input.txt").read()

monkeys = {}
inspected = {}

for monkey in inp.split("\n\n"):
    monkey = monkey.splitlines()
    name = None
    for line in monkey:
        if line.startswith("Monkey"):
            name = line.split(" ")[1].split(":")[0]
            monkeys[name] = {}
            inspected[name] = 0
        elif line.startswith("  Starting"):
            startingItems = json.loads("["+line.split(": ")[1]+"]")
            monkeys[name]["startingItems"] = startingItems
        elif line.startswith("  Operation"):
            operation = line.split("= ")[1]
            monkeys[name]["operation"] = operation
        elif line.startswith("  Test"):
            test = line.split("by ")[1]
            monkeys[name]["test"] = int(test)
        elif line.startswith("    If true"):
            ifTrue = line.split("monkey ")[1]
            monkeys[name]["ifTrue"] = ifTrue
        elif line.startswith("    If false"):
            ifFalse = line.split("monkey ")[1]
            monkeys[name]["ifFalse"] = ifFalse

rounds = 10000
a =  reduce(mul, (monkey['test'] for key, monkey in monkeys.items()))

for i in range(rounds):
    for monkey, monkVal in monkeys.items():
        for item in monkVal['startingItems']:
            score = int(eval(f"{monkVal['operation'].replace('old', str(item))}"))
            score %= a
            if score%monkVal['test'] == 0:
                monkeys[monkVal['ifTrue']]['startingItems'].append(score)
            else:
                monkeys[monkVal['ifFalse']]['startingItems'].append(score)
            inspected[monkey] += 1
        monkeys[monkey]['startingItems'] = []

inspectedList = []
for monk, val in inspected.items():
    inspectedList.append(val)

inspectedList.sort()
monkeyBusiness = inspectedList[-1] * inspectedList[-2]
print(monkeyBusiness)