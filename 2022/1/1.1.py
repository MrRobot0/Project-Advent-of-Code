with open('1-input.txt', 'r') as file:
    countSet = 0
    highScore = 0
    for line in file:
        if line == "\n":
            if countSet > highScore:
                highScore = countSet
            countSet = 0
        else:
            countSet += int(line)
    print(highScore)