#Constants

points = {
    "Win": 6,
    "Draw": 3,
    "Lose": 0
}

scores = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

convert = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win"
}

doWin = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock"
}

doDraw = {
    "Rock": "Rock",
    "Paper": "Paper",
    "Scissors": "Scissors"
}

doLose = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}

#Variables
totalScore = 0

#Program
rounds = open("2-input.txt", "r")
for round in rounds:
    p1 = round[0]
    strat = round[2]

    do = ""

    if convert[strat] == "Win":
        do = doWin[convert[p1]]
    elif convert[strat] == "Draw":
        do = doDraw[convert[p1]]
    elif convert[strat] == "Lose":
        do = doLose[convert[p1]]

    totalScore += scores[do]
    totalScore += points[convert[strat]]


#Finally
rounds.close()
print(totalScore)