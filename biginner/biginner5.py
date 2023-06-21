from pwnlib.util.fiddling import xor

KEY1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
KEY2andKEY1 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
KEY2andKEY3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
FLAGandKEY1andKEY3andKEY2 = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

KEY123 = xor(KEY1,KEY2andKEY3)
flag = xor(FLAGandKEY1andKEY3andKEY2,KEY123)

print(format(flag.decode()))