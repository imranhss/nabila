infile=open("seinfeld.txt", "r")
string=infile.read()
infile.close()
print(string)

write_file=open("seinfeldOut1.txt", "w")
write_file.write(string)
write_file.close()
