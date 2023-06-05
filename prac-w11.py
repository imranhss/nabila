infile=open("G:\\Nabila AU\\Practice\\resource\\bye.txt", "r")

stringList = infile.readlines() # make whole text as list

for string in stringList:
    strSplit = string.split() # split word by word
    # print(strSplit) 
    n1 = int(strSplit[0])
    n2 = int(strSplit[1])

    diff = abs(n2 - n1)
    print(diff)

infile.close()


