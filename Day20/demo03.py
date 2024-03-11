import matplotlib.pyplot as plt
import csv
plt.rc('font',family="Microsoft JhengHei")
file=open('data.csv')
read=csv.reader(file)
header=next(file)
print(header)
x=[]    # 2020,2021,2022
y=[]
for row in read:
    print(row)
    x.append(int(row[0]))
    y.append([int(row[1]),int(row[2]),int(row[3])])
plt.plot(x,y,label=["張三","李四","王五"])
plt.legend()
plt.show()