from Crypto.Util.number import long_to_bytes
# message: HELLO
# ascii bytes: [72, 69, 76, 76, 79]
# hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
# base-16: 0x48454c4c4f
# base-10: 310400273487

msg = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

ans = long_to_bytes(msg)
print(ans)
#ans = b'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'