from pwnlib.util.fiddling import xor

key = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
# print(key)
for i in range(256):
    
    flag = xor(key,i)
    flag_t = flag.decode()
    if flag_t[:7] == 'crypto{': #大量に文字が出るため，形式を満たしたflagのみ抽出
        print(flag)
# print(xor(key,1))
