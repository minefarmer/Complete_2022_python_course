import numpy as np




'''         Basic Slicing
import numpy as np
my_list = [[1,2,3], [2,3,5], [1,3,5]]
np_array = np.array( my_list )

#   [atart : end, , start : end ]

print(np_arr[1:2, 2])


'''



'''         Copy Function
import numpy as np
np_arr = np.array([[1,2,3], [2,3,5], [1,3,5]])
np_subarr = np_arr[1:2, 0:]
np_subarr[0,1] = 10
print(np_arr)
print( np_subarr)

'''

# np_rand = np.random.random((3,3))
# print(np_rand)  # [[0.57658906 0.23280631 0.56092117]
               # [0.88678054 0.71917141 0.88642204]
               # [0.54664565 0.82087573 0.54313106]]
        # # second run
        # [[0.43019281 0.22091733 0.41690699]
        # [0.45411462 0.61695872 0.05184207]
        # [0.53338773 0.67838238 0.0087478 ]]



np.random.seed(0)
np_rand = np.random.random((3,3))
# print(np_rand)  # [[0.5488135  0.71518937 0.60276338]
#                 # [0.54488318 0.4236548  0.64589411]
#                 # [0.43758721 0.891773   0.96366276]]
#             # # second run  ## same as above
#                 # [[0.5488135  0.71518937 0.60276338]
#                 # [0.54488318 0.4236548  0.64589411]
#                 # [0.43758721 0.891773   0.96366276]]
                
# print(np_rand[0:2 , 0:2])  # [[0.5488135  0.71518937]
#                            # [0.54488318 0.4236548 ]]

# print(np_rand[0:3 , 0:2])  # [[0.5488135  0.71518937]
#                            # [0.54488318 0.4236548 ]
#                            # [0.43758721 0.891773  ]]
                           
                           
                           
np_sub_rand = np.copy(np_rand[0:3 , 0])
print (np_sub_rand)  # [0.5488135  0.54488318 0.43758721]

np_sub_rand[0] = 1000

print(np_sub_rand)  # [1.00000000e+03 5.44883183e-01 4.37587211e-01]

print(np_sub_rand)  # [1.00000000e+03 5.44883183e-01 4.37587211e-01]
