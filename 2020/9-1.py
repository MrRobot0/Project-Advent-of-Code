array = "35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576"
array = array.split(',')

array2 = []
count = 0
arraystring = ""

for x in array:
    if array.index(x) == (len(array) - 1):
        arraystring += f"{x},"
        arraystring = arraystring[0:(len(arraystring) - 1)]
        array2.append(arraystring.split(','))
    if count < 5:
        arraystring += f"{x},"
        count += 1
    else:
        arraystring = arraystring[0:(len(arraystring) - 1)]
        array2.append(arraystring.split(','))
        arraystring = ""
        count = 0
        arraystring += f"{x},"
        count += 1

notvalid = []

for check1 in range(0, len(array2), 2):
    for check2 in range(1, len(array2), 2):
        for finalnumber in array2[check2]:
            valid = False
            for number1 in array2[check1]:
                for number2 in array2[check1]:
                    print(f"{int(finalnumber)}: {int(number1)} + {int(number2)} == {int(number1) + int(number2)}")
                    if int(number1) + int(number2) == int(finalnumber):
                        valid = True
            if not valid:
                notvalid.append(finalnumber)

for x in array2:
    print(x)

for check1 in range(0, len(array2), 2):
    for check2 in range(1, len(array2), 2):