#Setup
#Not using 2's complement, just using a leading 1 for negative
#Sign and magnitude
#int to 16bit
#fetch decode execute
#16 bit word, for instructions it's 8bit opcode and 8bit operand
totalMem = 0
locations = 32
#IO
debug = False
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
        ##print(binary)
        binary = binary[1:16]
        ##print(binary)
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
    ##print("JMPlus")
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
    ##acc = acc * 2

def cmp(op):
    global acc
    op = fullBinToInt(op)
    if acc > op:
        acc = 1
    elif acc == op:
        acc = 0
    else:
        acc = -1

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
        if debug: print("ADD"+str(operand))
        ##print(str(operand)+"operand")
        addLoc(operand)
    if opcode == "2":
        if debug: print("SUB "+str(operand))
        ##print(str(operand)+"operand")
        subLoc(operand)
    if opcode == "3":
        if debug: print("STR "+str(operand))
        storAcc(operand)
    if opcode == "4":
        if debug: print("JMZ "+str(operand))
        jumpIfZero(operand)
    if opcode == "5":
        if debug: print("JPL "+str(operand))
        jumpIfPlus(operand)
    if opcode == "6":
        if debug: print("JMP "+str(operand))
        jump(operand)
    if opcode == "7":
        if debug: print("LDA "+str(operand))
        loadAcc(operand)
    if opcode == "8":
        if debug: print("OUT "+str(operand))
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
    if opcode == "13":
        cmp(operand)
    if opcode == "0":
        print("End of program")
        ProgCounter = locations+1

memory[0] = '0000011100001010'
memory[1] = '0000001000001011'
memory[2] = '0000001100001010'
memory[3] = '0000010100000101'
memory[4] = '1000000000000000'
memory[5] = '0000011100001100'
memory[6] = '0000100000000000'
memory[7] = '0000101100000001'
memory[8] = '0000001100001100'
memory[9] = '0000011000000000'
memory[10] = '0000000000010000'
memory[11] = '0000000000000001'
memory[12] = '0000000000000001'

while ProgCounter < locations:
    #print(memory[ProgCounter])
    #print(acc)
    if fetch() == '1000000000000000':
        print("End of program")
        ProgCounter = locations+1
        break
    else:
        decodeExec(fetch())
        ProgCounter = int(ProgCounter) + 1
        
