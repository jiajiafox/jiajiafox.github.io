import numpy as np

eye_array=np.eye(3)
print(eye_array)

my_view=eye_array.view()
my_view[:]=4
print(my_view)
print(eye_array)

# view是複製+更改原有資料