import matplotlib.pyplot as plt
plt.rc('font',family="Microsoft JhengHei")
color=["#004B97","#930000","#9F0050","#EAC100"]
time_data={'Facebook':120,'Youtube':40,'Instagram':40,'Snapchar':28}
social_madia=list(time_data.keys())
time_spend=list(time_data.values())

#長條圖
# plt.bar(social_madia,time_spend,color=["#004B97","#930000","#9F0050","#EAC100"])
plt.bar(social_madia,time_spend,color=color)
plt.title("social_madia")
plt.xlabel('social_madia')
plt.ylabel("time_spend")
plt.show()