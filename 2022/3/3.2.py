import string

#Constants
alphabet = string.ascii_letters
lines = open("3-input.txt", "r")

#Variables
total = 0
group = {
    1: "",
    2: "",
    3: "",
    "count": 1
}

#Methods
def resetGroups():
    group[1] = ""
    group[2] = ""
    group[3] = ""
    group["count"] = 1

#Program
for line in lines:
    if group["count"] == 3:
        group[3] = line

        matchingLetters = []
        for letter in group[1]:
            index = group[2].find(letter)
            if index != -1:
                matchingLetters.append(group[2][index])

        for letter in matchingLetters:
            index = group[3].find(letter)
            if index != -1:
                total += alphabet.find(group[3][index]) + 1
                break

        resetGroups()
    else:
        group[group["count"]] = line
        group["count"] += 1


#finally
lines.close()
print(total)