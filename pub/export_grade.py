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
nc.write('{"supported": ["DH64", "DH2"]}')
for i in range(2):
    print(nc.read().decode('utf-8').split('\n'))
#send to alice
nc.write('{"chosen": "DH64"}')
print("-"*6)
for i in range(2):
    print(nc.read().decode('utf-8').split('\n'))