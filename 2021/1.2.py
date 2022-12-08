f = open("D:\OneDrive\OneDrive - Office 365 Fontys\______________\Projects\Project Advent of Code\\2021\\1 - input.txt")
groups = []
index = [0]

for depth in f:
    depth = int(depth)
    for i in index:
        try:
            groups[i] += depth
        except:
            groups.append(depth)
    
    if len(index) != 3:
        index.append(index[-1] + 1)
    else:
        index.append(index[-1] + 1)
        index.pop(0)

numberOfIncreases = 0
previousRecording = 0

for depth in groups:
    if depth > previousRecording and previousRecording != 0:
        numberOfIncreases += 1
    previousRecording = depth

print(numberOfIncreases)