#Setup
#Not using 2's complement, just using a leading 1 for negative
#int to 16bit
#fetch decode execute
totalMem = 0
locations = 48
#IO

acc = 0 #Accumulator is in base 10 for simplicity, and so that signs works.
ProgCounter = 0

#Functions
def showRAMInt(mem_):
    intMem = list()
    for item in mem_:
        intMem.append(fullBinToInt(item))
    return(intMem)

def prepareRAM(locations):
    mem = list()
    for i in range(locations):
        mem.append("0000000000000000")
    totalMem = (locations/2)*8
    return(mem)

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

#Initialise
memory = prepareRAM(locations)
totalMem = len(memory)*2
print(str(totalMem)+" bytes prepared ("+str(locations)+" locations)")
print(memory)

#Instructions
def addLoc(loc):
    loc = str(loc)
    #print(loc+" loc")
    global acc
    #print(lookUpLoc(loc)+"lookedup")
    data = lookUpLoc(loc)
    #print(data+"data")
    #print(fullBinToInt(data))
    #print(str(acc)+"AccumulatorAdd")
    #print("Attempted to add "+str(int(acc))+" (acc) and "+str(int(fullBinToInt(data)))+" which gives "+str(int(fullBinToInt(data))+int(acc)))
    acc = int(int(acc) + int(fullBinToInt(data)))
    #print("AccumPostAdd "+str(acc))

def subLoc(loc):
    loc = str(loc)
    global acc
    data = lookUpLoc(loc)
    #print(fullBinToInt(data))
    acc = acc - int(fullBinToInt(data))

def lookUpLoc(loc):
    global memory
    global acc
    loc = int(loc)
    #print("triedtolookup "+str(loc))
    return(memory[loc])

def storAcc(loc):
    global memory
    global acc
    #print(str(loc)+"location for store")
    #print(str("AccforStore"+str(acc)))
    loc = int(loc)
    memory[loc] = fullIntToBin(acc)

def jumpIfZero(loc):
    global acc
    loc = str(loc)
    if acc == 0:
        ProgCounter = int(loc)-1 #Must have a -1, as jump increments the counter as the counter increments after running...
        
    
def jumpIfPlus(loc):
    #print("JMPlus")
    global acc
    global ProgCounter
    loc = str(loc)
    if acc >= 0:
        ProgCounter = int(loc)-1 #And again here

def jump(loc):
    loc = str(loc)
    global ProgCounter
    ProgCounter = int(loc)-1 #Here also

def loadAcc(loc):
    global memory
    global acc
    acc = fullBinToInt(memory[int(loc)])

def output(form):
    global acc
    print(chr(acc))
    if form == 0:
        print(acc)
    if form == 1:
        print(chr(acc))
#Cycle
def fetch():
    #print("fetch")
    #print(lookUpLoc(ProgCounter)+" lookup")
    return(lookUpLoc(ProgCounter))

def decodeExec(data):
    global acc
    ##print("check")
    #print(data+"data")
    #print(fullBinToInt(data))
    dataInt = fullBinToInt(data)
    dataInt = str(dataInt)
    #print(dataInt+"dataInt")
    argument = dataInt[1:len(dataInt)]
    #print(argument)
    instruction = dataInt[0]
    #print(instruction)
    if instruction == "1":
        #print("ADD")
        #print(str(argument)+"argument")
        addLoc(argument)
    if instruction == "2":
        #print("SUB")
        #print(str(argument)+"argument")
        subLoc(argument)
    if instruction == "3":
        #print("STR")
        storAcc(argument)
    if instruction == "4":
        #print("JMZ")
        jumpIfZero(argument)
    if instruction == "5":
        #print("JPL")
        jumpIfPlus(argument)
    if instruction == "6":
        #print("JMP")
        jump(argument)
    if instruction == "7":
        #print("LDA")
        loadAcc(argument)
    if instruction == "8":
        #print("OUT")
        #print(acc)
        output(argument)
    elif instruction == "0":
        print("End of program")

memory[0] = '0000001011011101'
memory[1] = '0000000001010001'
memory[2] = '0000001011011110'
memory[3] = '0000000001010001'
memory[4] = '0000001011011111'
memory[5] = '0000000001010001'
memory[6] = '0000001011100000'
memory[7] = '0000000001010001'
memory[8] = '0000001011100001'
memory[9] = '0000000001010001'
memory[10] = '0000001011011110'
memory[11] = '0000000001010001'
memory[12] = '0000001011011111'
memory[13] = '0000000001010001'
memory[14] = '0000001011100010'
memory[15] = '0000000001010001'
memory[16] = '0000001011100011'
memory[17] = '0000000001010001'
memory[18] = '0000001011100100'
memory[19] = '0000000001010001'
memory[20] = '0000001011100101'
memory[21] = '0000000001010001'
memory[22] = '0000001011011110'
memory[23] = '0000000001010001'
memory[24] = '0000001011100001'
memory[25] = '0000000001010001'
memory[26] = '0000001011011111'
memory[27] = '0000000001010001'
memory[28] = '0000001011100110'
memory[29] = '0000000001010001'
memory[30] = '0000001011100111'
memory[31] = '0000000001010001'
memory[32] = '1000000000000000'
memory[33] = '0000000001010111'
memory[34] = '0000000001100101'
memory[35] = '0000000000100000'
memory[36] = '0000000001100001'
memory[37] = '0000000001110010'
memory[38] = '0000000001101110'
memory[39] = '0000000001110101'
memory[40] = '0000000001101101'
memory[41] = '0000000001100010'
memory[42] = '0000000000110001'
memory[43] = '0000000000100001'
print(showRAMInt(memory))
while ProgCounter < locations:
    #print(memory[ProgCounter])
    #print(acc)
    if fetch() == '1000000000000000':
        print("End of program")
        break
    else:
        decodeExec(fetch())
        ProgCounter = int(ProgCounter) + 1
        
