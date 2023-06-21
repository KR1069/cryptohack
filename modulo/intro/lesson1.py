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
    x, y = t, s - q*t
    return x, y, d