f = open("newFile.txt", "w")
f.close

for i in range(0,10):
    i+=1
    data= f"{i} line \n"
    f.write(data)

# while True:
#     line = f.readline()
#     line = line.strip()
#     if not line: break
#     print(line)


f.close
f = open("newFile.txt", "a")

for i in range(0,10):
    i+=1
    data= f"{i} new line\n"
    f.write(data)
    
f = open("newFile.txt", "r")

line2 = f.read()
print(line2)
# fstline = f.readline()
# sndline = f.readline()
# print(fstline)
# print(sndline)
