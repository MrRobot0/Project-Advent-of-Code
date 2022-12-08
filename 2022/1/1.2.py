with open('1-input.txt', 'r') as file:
    countSet = 0
    score1 = 0
    score2 = 0
    score3 = 0
    scoresRepeat = []
    for line in file:
        if line == "\n":
            if countSet > score1:
                score1 = countSet
                scoresRepeat.append(countSet)
                print(f"1: HigherScore! score= 1: {score1} 2: {score2} 3: {score3} countSet: {countSet}")
            elif countSet > score2:
                score2 = countSet
                scoresRepeat.append(countSet)
                print(f"2: HigherScore! score= 1: {score1} 2: {score2} 3: {score3} countSet: {countSet}")
            elif countSet > score3:
                score3 = countSet
                scoresRepeat.append(countSet)
                print(f"3: HigherScore! score= 1: {score1} 2: {score2} 3: {score3} countSet: {countSet}")
            else:
                print(f"No higher score= 1: {score1} 2: {score2} 3: {score3} countSet: {countSet}")
            countSet = 0
        else:
            countSet += int(line)
    print(f"1: {score1} 2: {score2} 3: {score3}")
    print(f"Total: {score1 + score2 + score3}")
    for score in scoresRepeat:
        if score > score1:
            score1 = score
            print(f"1: HigherScore! score= 1: {score1} 2: {score2} 3: {score3} score: {score}")
        elif score > score2:
            if score == score1:
                break
            score2 = score
            print(f"2: HigherScore! score= 1: {score1} 2: {score2} 3: {score3} score: {score}")
        elif score > score3:
            if score == score1 or score == score2:
                break
            score3 = score
            print(f"3: HigherScore! score= 1: {score1} 2: {score2} 3: {score3} score: {score}")
    print(f"1: {score1} 2: {score2} 3: {score3}")
    print(f"Total: {score1 + score2 + score3}")