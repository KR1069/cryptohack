import requests

base_url = "https://aes.cryptohack.org/bean_counter/"
response = requests.get(url="%s/encrypt/" % (base_url)).json()
word_list = list(range(ord('a'),ord('z')+1)) + list(range(ord('0'),ord('9')+1)) +[ord("{"),ord("}")]
print(word_list)
# print(response)
# ciphertext = response['encrypted']
# print(len(ciphertext) )
# print(len(ciphertext) % 32)

# cipher_list = [ciphertext[32*i:32*(i+1)] for i in range((len(ciphertext) // 32)-1)]
# cipher_list.append(ciphertext[-(len(ciphertext) % 32):])
# # print(cipher_list[-1])
# print(bytes.hex(b"crypt{"))
print(len(b"crypt{"))
