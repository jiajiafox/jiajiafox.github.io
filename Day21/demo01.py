import matplotlib.pyplot as plt
plt.rc('font',family="Microsoft JhengHei")
"""
2,4
4,3
3,6
"""
#散佈圖
plt.title("散佈圖")
plt.scatter([2,4,3],[4,3,6],c="#328283",s=80,label="AAA")
plt.scatter([4,8,6],[8,6,12],c="#576605",s=80,label="BBB")
plt.legend()
plt.show()
