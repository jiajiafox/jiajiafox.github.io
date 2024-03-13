import matplotlib.pyplot as plt
import csv
plt.rc('font',family="Microsoft JhengHei")

file=open('person.csv')
read=csv.reader(file)
header=next(file)
print(header)