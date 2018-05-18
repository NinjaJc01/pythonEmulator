#Instructions to binary
address = input("Enter assembly file location:    ")
fileInstructions = open(address,"r")
fileBinary = open("BIN"+address,"a")
program = list()

def fullIntToBin(integer):
    if integer < 32768:
        if integer >= 0:
            lead = "0"
            stem = format(int(integer), '015b')
        else:
            lead = "1"
            stem = format(int(integer)*-1, '015b')
        return(lead+stem)
    else:
        raise(OverflowError)
    
def fullIntTo8bit(integer):
    if int(integer) >= 0:
        lead = "0"
        stem = format(int(integer),'7b').replace(" ","0")
    else:
        lead = "1"
        stem = format(int(integer)*-1,'7b').replace(" ","0")
    return(lead+stem)

def toAddress(program):
##    file = open("BINcode.txt","r")
##    fileList = list()
##    for line in file:
##        line = line.rstrip("\n")
##        fileList.append(line)
    counter = 0
    for i in program:
        print("memory["+str(counter)+"] = '"+i+"'")
        counter = counter + 1
##    file.close()


for line in fileInstructions:
    print(line.rstrip("\n"))
    line = line.rstrip("\n")
    instruction = (line.rstrip(" "))[0:3]
    argument = (line.rstrip(" "))[4:len(line)]
    if instruction == "ADD":
        currentInst = "1"
    elif instruction == "SUB":
        currentInst = "2"
    elif ((instruction == "STO") or (instruction == "STR") or (instruction == "STA")):
        currentInst = "3"
    elif instruction == "JMZ":
        currentInst = "4"
    elif instruction == "JPL":
        currentInst = "5"
    elif instruction == "JMP":
        currentInst = "6"
    elif instruction == "LDA":
        currentInst = "7"
    elif instruction == "OUT":
        currentInst = "8"
    elif instruction == "INP":
        currentInst = "9"
    elif instruction == "ASR":
        currentInst = "10"
    elif instruction == "ASL":
        currentInst = "11"
    elif instruction == "MUL":
        currentInst = "12"
    elif instruction == "CMP":
        currentInst = "13"
    elif instruction == "DAT":
        currentInst = "0"
    elif instruction == "HLT":
        toBinary = "1000000000000000"
    ##print(instruction)
    ##currentInst.append(argument)
    
    if instruction == "HLT":
        ##toBinary = "1000000000000000"
        program.append("1000000000000000")
    else:
        toBinary = "".join(currentInst)
        program.append(fullIntTo8bit(currentInst)+fullIntTo8bit(argument))
    #print(toBinary+"toBin")
    ##print(currentInst)
    ##print((argument))
    
    ##toBinary = fullIntToBin(int(toBinary))
    ##program.append(toBinary)
    ##print(currentInst)

for codeLine in program:
    print(codeLine, file=fileBinary)
toAddress(program)
fileInstructions.close()
fileBinary.close()
#fileInstructions.readline()

