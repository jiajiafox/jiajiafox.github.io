"""
1=(1,2),(2,5),(3,3)
2=(1,5),(2,3),(3,3)
"""

import matplotlib.pyplot as plt
plt.rc('font',family="Microsoft JhengHei")
plt.title("3月業務業績表")   # 設置圖表標題
plt.xlabel("項目")          # 設置 X 軸標籤
plt.ylabel("金額")          # 設置 Y 軸標籤
plt.plot([1,2,3],[[2,5],[5,3],[3,3]],label=["業務一課","業務二課"])  # plt.plot()：繪製線條圖
plt.legend()      # 顯示圖例
plt.show()