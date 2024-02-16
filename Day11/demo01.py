# reduce(function,list)
import functools
list1=[1,2,3,4,5]

def fuc(a,b):
    return a+b

result=functools.reduce(fuc,list1)
print(result)