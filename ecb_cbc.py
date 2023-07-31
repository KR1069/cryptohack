import requests
from Crypto.Util.number import long_to_bytes
url_base = 'https://aes.cryptohack.org/ecbcbcwtf/'

response = requests.get(url='%s/encrypt_flag/%s' % (url_base,''.encode().hex())).json()
cipher_text = response['ciphertext']

print(cipher_text)

def decrypt_block(cipher_text):
    divided_cipher = [cipher_text[32*i:32*i+32] for i in range(len(cipher_text)// 32)]
    msg = b''
    for i in range(len(divided_cipher)-1):
        
        responce2 = requests.get(url='%s/decrypt/%s'% (url_base,divided_cipher[i+1])).json()
        msg  +=  long_to_bytes(int(divided_cipher[i],16) ^ int(responce2['plaintext'],16))
    print(msg)
    

decrypt_block(cipher_text)