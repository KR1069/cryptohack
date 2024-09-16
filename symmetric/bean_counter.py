import requests
from pwn import xor
base_url = "https://aes.cryptohack.org/bean_counter/"
response = requests.get(url="%s/encrypt/" % (base_url)).json()
word_list = list(range(ord('a'),ord('z')+1)) + list(range(ord('0'),ord('9')+1)) +[ord("{"),ord("}")]
print(word_list)
# print(response)
#pngであることを示すpngsignature + pngの画像の情報を記すihdrという情報に分かれている
png_header = "89504e470d0a1a0a" + "0000000d49484452" 
ciphertext = bytes.fromhex(response['encrypted'])

key = xor(bytes.fromhex(png_header),(ciphertext[:16]))
with open('./flag.png','wb')as f:
   f.write(xor(ciphertext,key))
# print(png_header)
# print(len(ciphertext) )
# print(len(ciphertext) % 32)

# cipher_list = [ciphertext[32*i:32*(i+1)] for i in range((len(ciphertext) // 32)-1)]
# cipher_list.append(ciphertext[-(len(ciphertext) % 32):])
# # print(cipher_list[-1])
# print(bytes.hex(b"crypt{"))
print(len(b"crypt{"))
