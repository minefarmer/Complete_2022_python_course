import numpy as np

my_list = [1,2,3]

my_arr = np.asarray(my_list)
print(my_arr)  # [1 2 3]
print(my_arr.dtype)  # int32
print(my_arr.shape)  # (3,)

np_zeros = np.zeros((5,5))
print(np_zeros)  # [[0. 0. 0. 0. 0.]
                    # [0. 0. 0. 0. 0.]
                    # [0. 0. 0. 0. 0.]
                    # [0. 0. 0. 0. 0.]
                    # [0. 0. 0. 0. 0.]]


np_zeros = np.zeros((5,5), dtype = int)
print(np_zeros)  # [[0 0 0 0 0]
                # [0 0 0 0 0]
                # [0 0 0 0 0]
                # [0 0 0 0 0]
                # [0 0 0 0 0]]

np_ones = np.ones((5,5))
print(np_ones)  # [[1. 1. 1. 1. 1.]
                # [1. 1. 1. 1. 1.]
                # [1. 1. 1. 1. 1.]
                # [1. 1. 1. 1. 1.]
                # [1. 1. 1. 1. 1.]]

np_range = np.arange(start = 2, step = 2 , stop = 20)
print(np_range)  # [ 2  4  6  8 10 12 14 16 18]

np_linspace = np.linspace(start = 2 , stop = 20 , num = 5)
print(np_linspace)  # [ 2.   6.5 11.  15.5 20. ]
