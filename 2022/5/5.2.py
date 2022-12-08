input = open("5-input.txt")
stacks = {
    1: ["B", "G", "S", "C"],
    2: ["T", "M", "W", "H", "J", "N", "V", "G"],
    3: ["M", "Q", "S"],
    4: ["B", "S", "L", "T", "W", "N", "M"],
    5: ["J", "Z", "F", "T", "V", "G", "W", "P"],
    6: ["C", "T", "B", "G", "Q", "H", "S"],
    7: ["T", "J", "P", "B", "W"],
    8: ["G", "D", "C", "Z", "F", "T", "Q", "M"],
    9: ["N", "S", "H", "B", "P", "F"]
}

for i in input:
    i = i.replace("move", "").replace("from", "").replace("to", "").strip().split("  ")
    i = [eval(x) for x in i]
    order = []
    for x in range(i[0]):
        order.append(stacks[i[1]][-1])
        stacks[i[1]].pop(-1)
    order.reverse()
    for o in order:
        stacks[i[2]].append(o)

printLastStacks = ""
for stack in stacks.values():
    printLastStacks += f"{stack[-1]}"

print(printLastStacks)