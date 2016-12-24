file = open("BINcode.txt","r")
fileList = list()
for line in file:
    line = line.rstrip("\n")
    fileList.append(line)
counter = 0
for i in fileList:
    print("memory["+str(counter)+"] = '"+i+"'")
    counter = counter + 1
file.close()
