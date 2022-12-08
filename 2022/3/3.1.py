import string

#Constants
alphabet = string.ascii_letters
lines = open("3-input.txt", "r")

#Variables
total = 0

#Program
for line in lines:
    halfLength = int(len(line) / 2)
    compartmentOne = line[:halfLength]
    compartmentTwo = line[halfLength:]

    for x in compartmentOne:
        index = compartmentTwo.find(x)
        if index != -1 and compartmentTwo[index] == compartmentOne[compartmentOne.find(x)]:
            total += alphabet.find(compartmentTwo[index]) + 1
            break
        
#finally
lines.close()
print(total)