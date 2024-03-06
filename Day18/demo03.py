import numpy as np
two_array=np.array([[1,3,5,7],
                    [2,4,6,8],
                    [10,11,12,13]])

print(two_array[2][2])      # 12
print(two_array[2,2])       # 12
print(two_array[2])         # [10 11 12 13]
print(two_array[2],[20])    # [10 11 12 13] [20]
