mathList = ""
mathB = 0
verCount = 7
for n in range(1,106):
    mathL = "{:04d}".format(n)
    if (n - 1) // verCount != mathB :
        mathList = mathList + "\n"
        mathB = n // verCount
    if mathL[-1] == "7" or mathL[-2] == "7" or mathL[-3] == "7" or n % 7 == 0:
        mathL = "*" + mathL[1] + mathL[2] + mathL[3]
    if mathL[0] == "0":
        mathL = " " + mathL[1] + mathL[2] + mathL[3]
    if mathL[1] == "0" and n < 100:
        mathL = mathL[0] + " " + mathL[2] + mathL[3]
    if mathL[2] == "0" and n < 100:
        mathL = mathL[0] + mathL[1] + " " + mathL[3]
    if mathList == "" :
        mathList = mathL + "  "
    else :
        mathList = "{}{}  ".format(mathList, mathL)

print(mathList)


