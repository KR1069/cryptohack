from Crypto.Util.number import long_to_bytes
import hashlib
with open("private_key.key","r")as f:
    rsa = f.readline().split(" ")
    N = int(rsa[2])
    d = int((f.readline().split(" "))[2])
    # print(N)
    
    # print(d)
    msg = b'crypto{Immut4ble_m3ssag1ng}'
    hs = pow(int(hashlib.sha256(msg).hexdigest(),16),d,N)
    print(hs)
# for line in rsa:
    
#     print(line[0])