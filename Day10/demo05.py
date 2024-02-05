fn1=lambda :120
print(fn1())
fn2=lambda a:a
print(fn2(200))
fn3=lambda a,b,c=100 : a+b+c
print(fn3(10,20))   #沒有回傳值，c就用預設值100
print(fn3(10,20,30))    #有給回傳值，就會覆蓋預設值