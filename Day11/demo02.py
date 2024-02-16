# filter(function,list)   過濾、攔截、阻攔

list1=[1,10,20,30,40]

def func(x):
    return x%2==0

x=filter(func,list1)
# print(x)          #記憶體位置
# print(type(x))    #型式為filter
print(list(x))      #結構為list