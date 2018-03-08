#Setup
#Not using 2's complement, just using a leading 1 for negative
#Sign and magnitude
#int to 16bit
#fetch decode execute
#16 bit word, for instructions it's 8bit opcode and 8bit operand
totalMem = 0
locations = 128
#IO
if locations > 512:
    raise(ValueError)

acc = 0 #Accumulator is in base 10 for simplicity, and so that +- works.
ProgCounter = 0 # base 10, because simplicity

#Functions
def showRAMInt(mem_):
    intMem = list()
    for item in mem_:
        intMem.append(fullBinToInt(item))
    return(intMem)

def prepareRAM(locations):
    global totalMem
    mem = list()
    for i in range(locations):
        mem.append("0000000000000000")
    totalMem = (locations)*2
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

def full8bitToInt(binary):
    sign = binary[0]
    magnitude = binary[1:8]
    val = int(magnitude,2)
    if sign == "0":
        return(val)
    else:
        return(-1*val)


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
##totalMem = len(memory)*2
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
    if form == "0":
        print(acc)
    if form == "1":
        print(chr(acc))
        
def inp():
    global acc
    inp_ = input("Input required:    ")
    try:
        inp_ = int(inp_)
        acc = inp_
    except:
        raise ValueError
    
def mult(loc):
    global memory
    global acc
    acc = acc*(memory[int(loc)])

def asr():
    global acc
    accBin = fullIntToBin(acc)
    accBin = "0"+accBin[1:16]
    acc = fullBinToInt(accBin)

def asl():
    global acc
    accBin = fullIntToBin(acc)
    accBin = accBin[1:16]+"0"
    acc = fullBinToInt(accBin)

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
    opcodeBin = data[0:8]
    operandBin = data[8:16]
    opcode = str(full8bitToInt(opcodeBin))
    operand = str(full8bitToInt(operandBin))
    ##print(opcode)
    ##print(operand)
    if opcode == "1":
        #print("ADD")
        #print(str(operand)+"operand")
        addLoc(operand)
    if opcode == "2":
        #print("SUB")
        #print(str(operand)+"operand")
        subLoc(operand)
    if opcode == "3":
        #print("STR")
        storAcc(operand)
    if opcode == "4":
        #print("JMZ")
        jumpIfZero(operand)
    if opcode == "5":
        #print("JPL")
        jumpIfPlus(operand)
    if opcode == "6":
        #print("JMP")
        jump(operand)
    if opcode == "7":
        #print("LDA")
        loadAcc(operand)
    if opcode == "8":
        ##print("OUT")
        ##print(acc)
        output(operand)
    if opcode == "9":
        inp()
    if opcode == "10":
        asr()
    if opcode == "11":
        asl()
    if opcode == "12":
        mul(operand)
    elif opcode == "0":
        print("End of program")

memory[0] = '0000011100100001'
memory[1] = '0000100000000001'
memory[2] = '0000011100100010'
memory[3] = '0000100000000001'
memory[4] = '0000011100100011'
memory[5] = '0000100000000001'
memory[6] = '0000011100100100'
memory[7] = '0000100000000001'
memory[8] = '0000011100100101'
memory[9] = '0000100000000001'
memory[10] = '0000011100100010'
memory[11] = '0000100000000001'
memory[12] = '0000011100100011'
memory[13] = '0000100000000001'
memory[14] = '0000011100100110'
memory[15] = '0000100000000001'
memory[16] = '0000011100100111'
memory[17] = '0000100000000001'
memory[18] = '0000011100101000'
memory[19] = '0000100000000001'
memory[20] = '0000011100101001'
memory[21] = '0000100000000001'
memory[22] = '0000011100100010'
memory[23] = '0000100000000001'
memory[24] = '0000011100100101'
memory[25] = '0000100000000001'
memory[26] = '0000011100100011'
memory[27] = '0000100000000001'
memory[28] = '0000011100101010'
memory[29] = '0000100000000001'
memory[30] = '0000011100101011'
memory[31] = '0000100000000001'
memory[32] = '0000100000000000'
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

while ProgCounter < locations:
    #print(memory[ProgCounter])
    #print(acc)
    if fetch() == '1000000000000000':
        print("End of program")
        break
    else:
        decodeExec(fetch())
        ProgCounter = int(ProgCounter) + 1
        
