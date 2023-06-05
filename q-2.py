# question 02
myList=[]
lowestNumber=999999
highestNumber=0
averageNumber=0
totalNumber=0

for i in range(1,21):    #15 25 10 5
    input_item=int(input("Plse enter number "+str(i)+"\n"))
    myList.append(input_item)
    totalNumber +=input_item # totalNumber= totalNumber+i ---40+10
    if highestNumber<input_item: # 25<10
        highestNumber=input_item  #25
        
    if lowestNumber >input_item:  #10 > 5 
        lowestNumber=input_item  # 5

averageNumber=totalNumber / 20


print(myList)
print("Lowest number is ", lowestNumber, "\n")
print("Highest number is ", highestNumber, "\n")
print("Total number is ", totalNumber, "\n")
print("Average number is ", averageNumber, "\n")
