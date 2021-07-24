def init_rc4(key):
    index1 = 0
    index2 = 0
    table = [0 for _ in range(256)]
    for i in range(256):
        index2 = (key[index1 % len(key)] + table[i] + index2) & 0xff
        table[i],table[index2] = table[index2],table[i]
    return table

def rc4(enc,table):
    x = 0
    y = 0
    for i in range(len(enc)):
        x = (x + 1) & 0xff
        y = (table[x] + y) & 0xff
        table[x],table[y] = table[y],table[x]
        enc[i] ^= table[(table[x] + table[y]) & 0xff]
    return bytes(enc)

def do_rc4(enc,key):
    table = init_rc4(key)
    return rc4(enc,table)

key = getBytes(toAddr(0x00416000),0x4)
enc = bytearray(getBytes(toAddr(0x00416008),0x146))
decrypted_conf = do_rc4(enc,key)
print(repr(decrypted_conf))
print(decrypted_conf)