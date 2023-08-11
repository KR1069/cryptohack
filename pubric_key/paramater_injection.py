from netcat import Netcat
import json
# start a new Netcat() instance
nc = Netcat('socket.cryptohack.org', 13371)
key_list = []

 # receive lines, print and solve fomula
for i in range(2):
    lines = nc.read().decode('utf-8').split('\n')
    print(lines)
Alice_dict = lines[0]
# print(Alice_dict)
#send_to_bob
nc.write(Alice_dict)
print('-'*6)
for i in range(2):
    lines = nc.read().decode('utf-8').split('\n')
    print(lines)
Bob_dict = lines[0]
Bob_fake_dict = '{"B": "0x01"}'

#send_to_alice
nc.write(Bob_fake_dict)
print('-'*6)
# recieve from _ alice 
print(nc.read())
lines = nc.read().decode('utf-8').split('\n')
iv = lines['iv']
encrypted_flag = lines['encrypted_flag']
    


     