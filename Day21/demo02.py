import matplotlib.pyplot as plt
import csv
plt.rc('font',family="Microsoft JhengHei")

file=open('person.csv')
read=csv.reader(file)
header=next(file)
data={"男":{"x":[],"y":[]},"女":{"x":[],"y":[]}}

for row in read:
    gender=row[0]
    data[gender]["x"].append(int(row[1]))
    data[gender]["y"].append(int(row[2]))
    print(data)

plt.scatter(data["男"]["x"],data["男"]["y"],label="男性")
plt.scatter(data["女"]["x"],data["女"]["y"],label="女性")
plt.legend()
plt.show()