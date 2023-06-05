# file_open=open("G:\\Nabila AU\\Practice\\resource\\bye.txt", "a")

# file_open.write(" Hello java")
# file_open.close()

# fi=open("G:\\Nabila AU\\Practice\\resource\\bye.txt", "r")
# print(fi.read())

# fi.close()

file_open=open("G:\\Nabila AU\\Practice\\resource\\bye.txt", "a")

fruit_list=["Mango", "Janm", "Apple", "Grape", "Barry"]

for fruit in fruit_list:
    file_open.write(fruit)

file_open.close()







# for line in t:
#     print(line, end='')

# while t !='':
#     print(t)
#     t=file_open.readline()
