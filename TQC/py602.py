# 串列(List)的運作(一維、二維以及多維)，撲克牌總和

sum=0
for i in range(5):
    s=input()
    if s=='J':sum+=11
    elif s=='Q':sum+=12
    elif s=='K':sum+=13
    elif s=='A':sum+=1
    else:sum+=int(s)
print(sum)