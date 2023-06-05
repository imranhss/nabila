infile=open("seinfeld.txt", "r")
string=infile.readlines()
infile.close()
print(string)

writeData=""

write_file=open("seinfeldOut3b.txt", "w")
for i in string:
    print(i)
    writeData +=i

write_file.write(writeData)
write_file.close()