import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.int16)
arr1 = np.array([[3,2,1],[6,5,4],[9,8,7]],dtype=np.int32)
print(arr)
print(arr1)
print('-'*20)
print(arr*arr1)
# zero_arr = np.zeros((3,3),dtype=np.int16)
# print(arr*zero_arr)