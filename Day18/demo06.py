import numpy as np
eye_array=np.eye(3)
print(eye_array)
print('------------')
# copy
my_view=eye_array.view()
print(my_view)
print('------------')

my_copy=eye_array.copy()
print(my_copy)