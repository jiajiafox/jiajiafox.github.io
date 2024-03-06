import numpy as np
eye_array=np.eye(3)

eye_array[1:]=3
eye_array[:,0]=4
# eye_array[:]=5
eye_array[0,0]=10
print(eye_array)

sort_array=np.sort(eye_array)   # 排序(由小到大)
print(sort_array)