with open('1-input.txt', 'r') as file:
    countSet = 0
    score1 = 0
    score2 = 0
    score3 = 0
    for line in file:
        if line == "\n":
            if countSet > score1:
                score1 = countSet
                print(f"1: HigherScore! score= 1: {score1} 2: {score2} 3: {score3} countSet: {countSet}")
            elif countSet > score2:
                score2 = countSet
                print(f"2: HigherScore! score= 1: {score1} 2: {score2} 3: {score3} countSet: {countSet}")
            elif countSet > score3:
                score3 = countSet
                print(f"3: HigherScore! score= 1: {score1} 2: {score2} 3: {score3} countSet: {countSet}")
            else:
                print(f"No higher score= 1: {score1} 2: {score2} 3: {score3} countSet: {countSet}")
            countSet = 0
        else:
            countSet += int(line)
    print("___________________________")
    with open('1-input.txt', 'r') as file2:
        for line2 in file2:
            if line2 == "\n":
                if countSet > score1:
                    score1 = countSet
                    print(f"1: HigherScore! score= 1: {score1} 2: {score2} 3: {score3} countSet: {countSet}")
                elif countSet > score2:
                    if countSet == score1:
                        break
                    score2 = countSet
                    print(f"2: HigherScore! score= 1: {score1} 2: {score2} 3: {score3} countSet: {countSet}")
                elif countSet > score3:
                    if countSet == score2 or countSet == score1:
                        break
                    score3 = countSet
                    print(f"3: HigherScore! score= 1: {score1} 2: {score2} 3: {score3} countSet: {countSet}")
                else:
                    print(f"No higher score= 1: {score1} 2: {score2} 3: {score3} countSet: {countSet}")
                countSet = 0
            else:
                countSet += int(line2)
    print(f"1: {score1} 2: {score2} 3: {score3}")
    print(f"Total: {score1 + score2 + score3}")