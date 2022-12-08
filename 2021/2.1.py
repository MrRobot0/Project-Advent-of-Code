f = open("D:\OneDrive\OneDrive - Office 365 Fontys\______________\Projects\Project Advent of Code\\2021\\2 - input.txt")

depth = 0
x = 0

for line in f:
    line = line.rstrip().split(" ")
    if line[0] == "forward":
        x += int(line[1])
    elif line[0] == "down":
        depth += int(line[1])
    elif line[0] == "up":
        depth -= int(line[1])

print(depth * x)    