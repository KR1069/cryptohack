import requests
from Crypto.Cipher import AES
import hashlib
import random

# KEY = hashlib.md5(keyword.encode()).digest()
# print(KEY)
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}

base_url = "https://aes.cryptohack.org/passwords_as_keys/"
wordlist_url = 'https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words'

r = requests.get(f'{base_url}/encrypt_flag')
response = requests.get(f'{wordlist_url}')
word_list = response.text.split('\n')

data = r.json()
ciphertext = data['ciphertext']

# ciphertext = bytes.fromhex(ciphertext)

for key in word_list:
    KEY = hashlib.md5(key.encode()).digest()
    password_hash = KEY.hex()
    plaintext = decrypt(ciphertext, password_hash)
    text_byte = bytes.fromhex(plaintext['plaintext'])
    text = ''.join([chr(int(byte)) for byte in text_byte])
    if text[:6] == 'crypto':
        print(text)
        break


