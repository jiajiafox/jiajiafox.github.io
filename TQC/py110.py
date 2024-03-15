# 基本程式設計，正n邊形面積計算

import math
n=int(input())
s=int(input())
ans=(n*s**2)/(4*math.tan(math.pi/n))
print("Area = %.4f"%ans)