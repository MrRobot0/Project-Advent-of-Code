f = open("6-input.txt")
lastFour = []
pos = 0
for line in f:
    for l in line:
        print(lastFour)
        if len(lastFour) == 14:
            if len(set(lastFour)) == len(lastFour):
                print(pos)
                break
            else:
                lastFour.pop(0)
                lastFour.append(l)
        else:
            lastFour.append(l)
        pos += 1