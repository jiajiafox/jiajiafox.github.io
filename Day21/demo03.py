import matplotlib.pyplot as plt
plt.rc('font',family="Microsoft JhengHei")

plt.title("長條圖")
time_data={'Facebook':120,'Youtube':40,'Instagram':40,'Snapchar':28}
social_madia=list(time_data.keys())
time_spend=list(time_data.values())

plt.bar(social_madia,time_spend)
plt.title("social_madia")
plt.xlabel('social_madia')
plt.ylabel("time_spend")
plt.show()