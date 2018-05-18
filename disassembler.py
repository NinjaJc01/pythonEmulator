##Disassembler
##memory array defined here
memory = [""]*20
memory[0] = '0000011100000111'
memory[1] = '0000001000001000'
memory[2] = '0000010100000100'
memory[3] = '1000000000000000'
memory[4] = '0000011100001001'
memory[5] = '0000101000000001'
memory[6] = '0000011000000000'
memory[7] = '0000000000001010'
memory[8] = '0000000000000001'
memory[9] = '0000000000000001'

##disassembler part
def full8bitToInt(binary):
    sign = binary[0]
    magnitude = binary[1:8]
    val = int(magnitude,2)
    if sign == "0":
        return(val)
    else:
        return(-1*val)

hex_ = list() 
for data in memory:
    if data == "": break
    opcodeBin = data[0:8]
    operandBin = data[8:16]
    hCode = hex(int(data, 2))[2:]
    if len(hCode) != 4:
        hCode = ("0"*(4-len(hCode)))+hCode
    hex_.append(hCode)
    opcode = str(full8bitToInt(opcodeBin))
    operand = str(full8bitToInt(operandBin))
    ##print(opcode)
    ##print(operand)
    
    if opcode == "1":
        print("ADD"+str(operand))
        
    elif opcode == "2":
        print("SUB "+str(operand))
        
    elif opcode == "3":
        print("STR "+str(operand))
        
    elif opcode == "4":
        print("JMZ "+str(operand))
        
    elif opcode == "5":
        print("JPL "+str(operand))
        
    elif opcode == "6":
        print("JMP "+str(operand))
        
    elif opcode == "7":
        print("LDA "+str(operand))

    elif opcode == "8":
        print("OUT "+str(operand))

    elif opcode == "9":
        print("INP "+str(operand))
        
    elif opcode == "10":
        print("ASR "+str(operand))
        
    elif opcode == "11":
        print("ASL "+str(operand))
        
    elif opcode == "12":
        print("MUL "+str(operand))
        
    elif opcode == "13":
        print("CMP "+str(operand))
        
    elif data == "1000000000000000":
        print("HLT")
    else:
        print("DAT "+str(operand))
print("\n".join(hex_))        
