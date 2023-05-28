
from pwnlib.util.fiddling import xor
# string1 = ord("l")
# string2 = ord("a")
# string3 = ord("b")
# string4 = ord("e")
# string5 = ord("l")
flag = xor('label',13)
print(flag)
print('crypto{{{}}}'.format(flag.decode()))


# print(string1,string2,string3,string4,string5)