# filter(function,list)   過濾、攔截、阻攔

list1=[1,10,20,30,40]

def func(x):
    if x%2==0:
        if x==10:
            return x
    else:
        return 0

x=filter(func,list1)
print(list(x))
