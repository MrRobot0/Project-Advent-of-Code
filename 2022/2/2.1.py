#Constants

points = {
    "Win": 6,
    "Draw": 3
}

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

checkWin = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

checkDraw = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

#Variables
totalScore = 0

#Program
rounds = open("2-input.txt", "r")
for round in rounds:
    p1 = round[0]
    p2 = round[2]

    if checkWin[p1] == p2:
        totalScore += points["Win"]
    elif checkDraw[p1] == p2:
        totalScore += points["Draw"]
        
    totalScore += scores[p2]
    
rounds.close()
print(totalScore)