mathList = ""
# 最大数
mathMax = 208
# 动态字符长度 为了保持字符串长度一致 比较好看 字符右对齐
mathLength = len("{}".format(mathMax)) + 3
# 基数
mathB = 0
# 每行字符串的个数
verCount = 10
for n in range(1,mathMax):
    mathL = "{}".format(n)
    if n % 7 == 0 or mathL[-1] == "7" :
        mathL = "*" + mathL
    while len(mathL) < mathLength :
        mathL = " " + mathL
    if (n - 1) // verCount != mathB :
        mathList = mathList + "\n"
        mathB = mathB + 1
    mathList = mathList + mathL

print(mathList)


