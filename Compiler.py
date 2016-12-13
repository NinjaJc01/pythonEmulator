#Instructions to binary
address = input("Enter assembly file location:    ")
fileInstructions = open(address,"r")
fileBinary = open("BIN"+address,"a")
program = list()
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

for line in fileInstructions:
    currentInst = list()
    print(line.rstrip("\n"))
    line = line.rstrip("\n")
    instruction = (line.rstrip(" "))[0:3]
    argument = (line.rstrip(" "))[4:9]
    if instruction == "ADD":
        currentInst.append("1")
    elif instruction == "SUB":
        currentInst.append("2")
    elif instruction == "STR":
        print("STR")
        currentInst.append("3")
    elif instruction == "JMZ":
        currentInst.append("4")
    elif instruction == "JPL":
        currentInst.append("5")
    elif instruction == "JMP":
        #print("JMP")
        currentInst.append("6")
    elif instruction == "LDA":
        #print("LDA")
        currentInst.append("7")
    elif instruction == "OUT":
        #print("OUT")
        currentInst.append("8")
        #print(acc)
        #output(argument)
    currentInst.append(argument)
    toBinary = "".join(currentInst)
    #print(toBinary+"toBin")
    toBinary = fullIntToBin(int(toBinary))
    program.append(toBinary)
    #print(currentInst)

for codeLine in program:
    print(codeLine, file=fileBinary)

fileInstructions.close()
fileBinary.close()
#fileInstructions.readline()

