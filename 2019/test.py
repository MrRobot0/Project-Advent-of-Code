fpath = "day_one_input.txt"
f= open("day1_output.txt", "w+")

with open(fpath) as fp:
    line = fp.readline()
    while line:
        f.write(str(float(line)//3-2))
        f.write("\n")
        line = fp.readline()

f.close()

#part 2-> summing data
total = 0

with open("day1_output.txt") as fp1:
    for line in fp1:
        try:
            num = float(line)
            total += num
        except ValueError:
            print("{} is not a number".format(line))

print(total)
