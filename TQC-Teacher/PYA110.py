import math
n=eval(input())
s=eval(input())
ans = (n*s**2)/(4*math.tan(math.pi/n))
print("Area = %.4f" %ans)