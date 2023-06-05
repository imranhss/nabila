# question 03

number_list=[]  #empty list

# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def reverse_numbers(number_list, top_index, bottom_index): # methods
    while top_index < bottom_index:    #top_index =2 <bottom_index=5    
        temp=number_list[top_index]    # temp=30
        number_list[top_index]=number_list[bottom_index] #bottom_index=5  60
        number_list[bottom_index] = temp 
        break

for i in range(10):     #0 1 2 3 4 5 6 7 8 9
    input_item=int(input("Plse enter number "+str(i+1)+"\n"))  
    number_list.append(input_item)


print(number_list)

topIndex=int(input("Enter top index\n"))
bottomIndex=int(input("Enter bottom index\n"))
reverse_numbers(number_list, topIndex, bottomIndex)

print("reverse list is ",number_list)

