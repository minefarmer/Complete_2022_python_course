import numpy as np

np_arr = np.arr = np.array([[1,2], [6,8]])
print(np_arr)  # [[1 2]
               # [6 8]]

np_arr = np.insert(arr = np_arr, obj = 1 , values = [3,4] , axis = 0 )
print(np_arr)  # [1 2]
               # [3 4]
               # [6 8]]
               
np_arr_insert = np.insert(arr = np_arr, obj = 1 , values = [3,4] , axis = 0 )
print(np_arr_insert)  # [[1 2]
                    # [3 4]
                    # [3 4]
                    # [6 8]]

np_arr_append = np.append(arr = np_arr, values = [3,4])  
print(np_arr_append)  # [[1 2]
                    # [3 4]
                    # [3 4]
                    # [6 8]]

np_arr_append = np.append(arr = np_arr, values = [[3,4], [1,2]], axis = 0)  
print(np_arr_append)  # [[1 2]
                    # [3 4]
                    # [6 8]
                    # [3 4]
                    # [1 2]]

np_arr_delete = np.delete(arr = np_arr , obj = 1, axis = 0)
print(np_arr_delete)  # [[1 2]
                    # [6 8]]
