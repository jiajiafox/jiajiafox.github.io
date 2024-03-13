import matplotlib.pyplot as plt
import numpy
plt.rc('font',family="Microsoft JhengHei")
wid=0.4
genres=["aaa","bbb","cccc","ddd","eeee"]
boys=[30,20,40,20,15]
girls=[20,40,20,15,35]
value=numpy.arange(len(genres))

# plt.bar(genres,boys,color="#004B97")
# plt.bar(genres,girls,bottom=boys,color="#9F0050")
plt.bar(value,boys,wid,label="BOYS",color="#004B97")
plt.bar(value+wid,girls,wid,label="GIRLS",color="#9F0050")
plt.show()