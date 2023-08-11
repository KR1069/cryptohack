from netcat import Netcat
import json
# start a new Netcat() instancenc 
nc = Netcat('socket.cryptohack.org', 13379)
i= 0
for i in range(2):
    lines = nc.read().decode('utf-8').split('\n')
    print(lines,type(lines))

#send to bob
print("-"*6)
nc.write('{"supported": ["DH1536", "DH64"]}')
for i in range(2):
    print(nc.read().decode('utf-8').split('\n'))
#send to alice
#DH64は計算量的に安全でないので、これを選択すればA = g^x=2^x mod pとなるAの秘密鍵xが求まる
nc.write('{"chosen": "DH64"}')
print("-"*6)
for i in range(2):
    print(nc.read().decode('utf-8').split('\n'))
    
# ['Intercepted from Alice: '] <class 'list'>
# ['{"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}', 'Send to Bob: '] <class 'list'>
# ------
# ['Intercepted from Bob: ']
# ['{"chosen": "DH64"}', 'Send to Alice: ']
# ------
# ['Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x198658d4a04121f"}', 'Intercepted from Bob: {"B": "0x154a08d1cbfef02"}', 'Intercepted from Alice: {"iv": "711b047f67316c00bae85e6527efeab5", "encrypted_flag": "9b6c4f5008068c0f0d6993ca11d1306e23f9d550e417608f9b12c9de69b61fc9"}', '']
# [''] 
# x satisfied A = 2^x mod p
#x = 5815547944080176533
#secret_key = B^x mod p = 14538612532375372590
#crypto{d0wn6r4d35_4r3_d4n63r0u5}