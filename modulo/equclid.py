#拡張ユークリッドの互除法
# ax + by = d = gcd(a,b)のx,yとdの解を求める。
import math

p = 26513 
q = 32321



def extgcd(a, b):
    if b == 0:
        return 1, 0, a
    
    q, r = a // b, a % b
    s, t, d = extgcd(b, r)
    print(s,t,d)
    x, y = t, s - q*t
    return x, y, d
#example
#3x + 2y = gcd(a,b)=1
# 3 / 2 = 2*1 + 1
#     2 /       1 = 2*1  + 0 
#
x,y,d = extgcd(7,5)
print(f'x={x} y={y} gcd={d}')