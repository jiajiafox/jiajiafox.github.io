
def method(**kwargs):   #字典結構
    print(kwargs)
# 字典結構  "name":"stanley","age":"26"
x=method(name="stanley",age=26,date="2024")


# fun=lambda **kwargs:kwargs
# print(fun(name="stanley",age=26,date="2024"))