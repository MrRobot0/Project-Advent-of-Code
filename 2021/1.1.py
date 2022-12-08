f = open("D:\OneDrive\OneDrive - Office 365 Fontys\______________\Projects\Project Advent of Code\\2021\\1 - input.txt")
numberOfIncreases = 0
previousRecording = 0
for depth in f:
    depth = int(depth)
    if depth > previousRecording and previousRecording != 0:
        numberOfIncreases += 1
    previousRecording = depth

print(numberOfIncreases)