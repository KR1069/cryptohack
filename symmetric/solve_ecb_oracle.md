問題

KEYとFLAGが不明
回答者の入力した文書をplaintext.出題者側が設定したメッセージをFLAGとする。
回答者にplaintext+Flagとなるメッセージの暗号文を渡すので、FLAGを見つけるという問題。
暗号方式はAESのECB_modeで暗号化されており、公開鍵も不明とする。

inputとして' 'を入れると32byteの16進数が返ってきた。つまり、flagは32byte以下。

プログラムの説明
```python
plaintext = ' ' * (FLAG_LENGTH - len(candidate)) + candidate + ' ' * (FLAG_LENGTH - len(candidate))
```
plaintext = '' *31 + char + ''*31
len(plaintext) = 63

plaintext+ flag  
1-16byte = ' '*16, 
17-32byte = ' ' *15 + b'char' 
33-48byte = ' '*16
49-64byte =  ' ' *15 + flag[0]
65-80byte = flag[1-16]
81-96byte = flag[17-31] + pading(0x00)

上記はplaintext + flagの並びになっている。ここで重要なのは0-32byteと33-64byteでchar == flag[0]だったら暗号化したときに同じ暗号文になること。なので,可能性のあるcharをしらみつぶしに選んでいき、hex形式の暗号文でcipher_text[:64] == cipher_text[64:128であればflag]flagの文字が特定できる.文字がわかったら適時次の文字で同じことをすれば,flagのすべての文字がわかる