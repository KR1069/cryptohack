import requests
from Crypto.Util.number import long_to_bytes
from pwn import xor
url_base = 'https://aes.cryptohack.org/symmetry/'

def encrypt_flag():

    response = requests.get(url='%s/encrypt_flag/' % (url_base)).json()
    cipher_text = response['ciphertext']
    return cipher_text
def encrypt(plain_text,iv):
    response = requests.get(url='%s/encrypt/%s/%s' % (url_base,plain_text,iv)).json()
    cipher_text = response['ciphertext']
    return cipher_text

cipher_text = encrypt_flag()
iv = cipher_text[:32]
cipher_list = [cipher_text[32:64],cipher_text[64:96],cipher_text[96:]]
print(iv)
print(cipher_list)
plain_text = bytes.hex(b' '* 32)
print(plain_text)
cipher_text2 = encrypt(plain_text,iv)
print(int((bytes.hex(b' '* 32)),16))
cipher_text2_list = [int((bytes.hex(b' '* 32)),16) ^ int((cipher_text2[32*i:32*(i+1)]),16) for i in range(len(cipher_text2)//32)]
print(cipher_text2_list[0])
flag_list = []
for i in range(len(cipher_text2_list)):
    flag_list.append(cipher_text2_list[i] ^ int(cipher_list[i],16))
print(long_to_bytes(flag_list[0]+flag_list[1]))
for i in flag_list:
    print(long_to_bytes(i))