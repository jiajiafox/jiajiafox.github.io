import numpy as np

eye_array=np.eye(3)
print(eye_array)

my_copy=eye_array.copy()
my_copy[:]=4
print(my_copy)
print(eye_array)

# copy是單純複製資料