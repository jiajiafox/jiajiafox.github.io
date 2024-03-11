# 圓餅圖

import matplotlib.pyplot as plt
plt.rc('font',family="Microsoft JhengHei")
plt.title("業務業績表(萬)")
plt.pie([20,50,30],labels=["張三","李四","王五"])
plt.legend()
plt.show()