import numpy as np

arr1=np.array([[1,2],[5,6]])
arr2=np.array([[11,12],[15,16]])

print(arr1)
print('----------')
print(arr2)
print('----------')

result=np.hstack((arr1,arr2))   #合併(二維度的合併)
print(result)