import requests

url_base = 'http://aes.cryptohack.org/ecb_oracle'

CHARACTER_SET = 'abcdefghijklmnopqrstuvwxyz0123456789_{}'
FLAG_LENGTH = 16 * 2

def hack():
  flag = ''
  for _ in range(FLAG_LENGTH):
    for char in CHARACTER_SET:
      candidate = flag + char
      plaintext = ' ' * (FLAG_LENGTH - len(candidate)) + candidate + ' ' * (FLAG_LENGTH - len(candidate))
      
      response = requests.get(url="%s/encrypt/%s" % (url_base, plaintext.encode().hex())).json()
      ciphertext = response['ciphertext']
      if ciphertext[:FLAG_LENGTH*2] == ciphertext[FLAG_LENGTH*2:FLAG_LENGTH*4]:
        flag = flag + char
        break
    if flag[-1] == '}':
      return flag
  return flag

if __name__ == '__main__':
  flag = hack()
  print(flag)