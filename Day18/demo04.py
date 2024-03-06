import numpy as np
empty_array=np.zeros((2,2))     #  [[0. 0.]   
# 預設位置 0                     #   [0. 0.]]

empty_array=np.ones((2,2))      #  [[1. 1.] 
# 預設位置 1                     #   [1. 1.]]

empty_array=np.eye(3)           # [[1. 0. 0.] 
                                 # [0. 1. 0.] 
                                 # [0. 0. 1.]]

empty_array[0,0]=3  # or empty_array[0][0]=3
empty_array[0]=3



print(empty_array)
