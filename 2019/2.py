from os import system, name
##PART1
solution = 0
looptimes = 1000

for i in range(looptimes):
    for j in range(looptimes):
        array = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,1,6,23,27,1,27,5,31,2,31,10,35,2,35,6,39,1,39,5,43,2,43,9,47,1,47,6,51,1,13,51,55,2,9,55,59,1,59,13,63,1,6,63,67,2,67,10,71,1,9,71,75,2,75,6,79,1,79,5,83,1,83,5,87,2,9,87,91,2,9,91,95,1,95,10,99,1,9,99,103,2,103,6,107,2,9,107,111,1,111,5,115,2,6,115,119,1,5,119,123,1,123,2,127,1,127,9,0,99,2,0,14,0]
        pos = 0
        posSafe = 0
        array[1] = i
        array[2] = j
        try:
            for x in array:
                if pos == posSafe:
                    posSafe += 4
                    if x == 1:
                        input1 = array[pos + 1]
                        input2 = array[pos + 2]
                        output = array[pos + 3]
                        array[output] = array[input1] + array[input2]
                    elif x == 2:
                        input1 = array[pos + 1]
                        input2 = array[pos + 2] 
                        output = array[pos + 3]
                        array[output] = array[input1] * array[input2]
                    elif x == 99:
                        break
                pos += 1
        except:
            break
        if array[0] == 19690720:
            solution = array

system("cls")
print("")
print("")
print("")
print("")
print("")
print(f"Yes! Found the solution.. {solution[0]} and the values are {solution[1]} and {solution[2]}")
print("")
print("")
print("")
print("")
print("")