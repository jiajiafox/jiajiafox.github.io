sum=0
for i in range(5):
    s=input()
    if s=='J':sum+=11
    elif s=='Q':sum+=12
    elif s=='K':sum+=13
    elif s=='A':sum+=1
    else: sum+=int(s)  #2~10
print(sum)