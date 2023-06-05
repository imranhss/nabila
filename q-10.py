infile=open("seinfeld.txt", "r")
string=infile.readlines()
infile.close()
print(string)

writeData=""

write_file=open("seinfeldOut2.txt", "w")
for i in string:
    writeData +=i

write_file.write(writeData)
write_file.close()
