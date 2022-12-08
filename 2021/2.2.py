f = open("D:\OneDrive\OneDrive - Office 365 Fontys\______________\Projects\Project Advent of Code\\2021\\2 - input.txt")

depth = 0
aim = 0
horizontalPos = 0

for line in f:
    line = line.rstrip().split(" ")
    if line[0] == "forward":
        horizontalPos += int(line[1])
        depth += aim * int(line[1])
    elif line[0] == "down":
        aim += int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])

print(f"{horizontalPos} * {depth} = {horizontalPos * depth}")