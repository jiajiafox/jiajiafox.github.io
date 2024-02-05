# map(function,參數)  ==>整合式寫法，高階內建函數(應用較廣)。
list1=[1,2,3,4,5,6,7]
def fun(x):
    return x**2
result=map(fun,list1)
print(list(result))
