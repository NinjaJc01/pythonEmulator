#Instructions to binary
address = input("Enter assembly file location:    ")
fileInstructions = open(address,"r")
fileBinary = open("BIN"+address,"a")
for line in fileInstructions:
    currentInst = list()
    #print(line.rstrip("\n"))
    line = line.rstrip("\n")
    instruction = (line.rstrip(" "))[0:3]
    argument = (line.rstrip(" "))[4:9]
    print(instruction)
    print(argument)
    if instruction == "ADD":
        currentInst.append("1")
    if instruction == "SUB":
        currentInst.append("2")
    if instruction == "STR":
        #print("STR")
        currentInst.append("3")
    if instruction == "JMZ":
        currentInst.append("4")
    if instruction == "JPL":
        currentInst.append("5")
    if instruction == "JMP":
        #print("JMP")
        currentInst.append("6")
    if instruction == "7":
        #print("LDA")
        currentInst.append("7")
    if instruction == "8":
        #print("OUT")
        currentInst.append("8")
        print(acc)
        output(argument)
#fileInstructions.readline()

def fullIntToBin(integer):
    if integer < 32768:
        if integer >= 0:
            lead = "0"
            stem = format(integer, '015b')
        else:
            lead = "1"
            stem = format(integer*-1, '015b')
        return(lead+stem)
    else:
        raise(OverflowError)

def fullBinToInt(binary):
    if binary[0] == "1":
        #it's negative
        print(binary)
        binary = binary[1:16]
        print(binary)
        return((int(binary, 2)*-1))
    elif binary[0] == "0":
        #it's postive
        binary = binary[1:16]
        return(int(binary, 2))
