import base64
#ASCiiテキストへの変更
msg = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
#16進数からbyte文字列にエンコード
msg_binary = bytes.fromhex(msg)
print(msg_binary)
#byte文字列からASCIIstringにエンコード
msg_ascii = base64.b64encode(msg_binary)
print(msg_ascii)