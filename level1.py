#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 


#TODO Add User Code Here

enc = []

addr = toAddr(0x1007e1)
inst = getInstructionAt(addr)
for _ in range(10):
	e = inst.getDefaultOperandRepresentation(1)
	enc.append(int(e,16))
	inst = inst.getNext()

print(''.join([chr(e ^ 0x7a) for e in enc]))