#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 


#TODO Add User Code Here

import string
import base64
default_b64_table = 'ABCDEFGHIJKLNMOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz0123456789+/'
print(len(default_b64_table))
def custom_b64decode(s,custom_table):
	s = s.translate(string.maketrans(custom_table,default_b64_table))
	return base64.b64decode(s)

b64_custom_table_addr = toAddr(0x100e00)
b64_custom_table_array = getBytes(b64_custom_table_addr,64)
b64_custom_table = ''.join([chr(b) for b in b64_custom_table_array])
enc = '4PpnRoanRomTze4SKPo+Zwd3IejS'
print(custom_b64decode(enc,b64_custom_table))