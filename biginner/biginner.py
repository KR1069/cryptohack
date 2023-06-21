msg = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

#hex型(16進数)からbyte型
msg_byte = bytes.fromhex(str(msg))
#byteからhex
# msghex = bytes.hex(msg)
print(msg_byte)