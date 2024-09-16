from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta
import requests
from pwn import xor
url_base = 'https://aes.cryptohack.org/flipping_cookie/'


#秒をとる

def encrypt():
    response = requests.get(url='%s/get_cookie/' % (url_base)).json()
    return response['cookie']

# def check_admin(cookie,iv):
#     r = requests.get(f"http://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{iv}")
#     return r.json()
def decrypt(cipher_text,iv):
    response = requests.get(url='%s/check_admin/%s/%s' % (url_base,cipher_text,iv)).json()
    return response


cookie_false = b"admin=False;expiry="[:16]
cookie_true = b"admin=True;expiry="[:16]

cipher_text = bytes.fromhex(encrypt())
iv = cipher_text[:16]
cipher = cipher_text[16:].hex()
iv_2nd = xor(cookie_false,cookie_true,iv).hex()
print(decrypt(cipher,iv_2nd)['flag'])

# list_cookie_false = [cookie_false[16*i:16*(i+1)] for i in range(len(cookie_false)//16)]

# print([[list_cookie_false[i][j] for j in range(16)] for i in range(len(cookie_false)//16)])

# print(list_cookie_false)
# print([chr(i) for i in range(len(cookie_false)//16)])
# list_cookie_true = [cookie_true[16*i:16*(i+1)] for i in range(len(cookie_true)//16)]
# print(list_cookie_true)