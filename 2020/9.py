array = "35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576"
array = array.split(',')

prev5Count = 0
prev5 = []
notvalid = []
firsttime = True
for number in array:
    if prev5Count < 5 and firsttime:
        prev5.append(number)
        prev5Count += 1
    elif prev5Count < 10:
        firsttime = False
        prev5.append(number)
        valid = False
        for prevNum1 in range(0, 5):
            for prevNum2 in range(0, 5):
                if int(prev5[prevNum1]) + int(prev5[prevNum2]) == number:
                    valid = True
        if valid == False:
            notvalid.append(number)
        prev5Count += 1
    else:
        prev5Count = 4
        for i in range(0,5):
            prev5.pop(0)
    print(f"{number}[{prev5Count}] + {prev5}")

print(notvalid)