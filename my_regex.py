#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 


#TODO Add User Code Here

def main():
	regex = askString('MyRegex','What do you want to search?')
	
	if not regex:
		print("[!] no inputs")
		return
	
	founds = findBytes(None,regex,-1)
	if not founds:
		print("[!] nothing found")
		return
	
	for found in founds:
		value = getDataAt(found).getValue()
		print('[+] {addr} -> {data}'.format(addr=found,data=value))

if __name__ == '__main__':
	main()
