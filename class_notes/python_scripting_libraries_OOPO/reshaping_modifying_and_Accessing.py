from turtle import clear
import numpy as np

my_arr = np.arange(20)
print(my_arr)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

my_arr_reshaped = np.reshape(my_arr, (5,4))
print(my_arr_reshaped)  # [[ 0  1  2  3]
                        # [ 4  5  6  7]
                        # [ 8  9 10 11]
                        # [12 13 14 15]
                        # [16 17 18 19]]

my_arr_reshaped = np.reshape(my_arr, (5,4) , order = "F" )
print(my_arr_reshaped)  # [[ 0  5 10 15]
                    # [ 1  6 11 16]
                    # [ 2  7 12 17]
                    # [ 3  8 13 18]
                    # [ 4  9 14 19]]


# my_arr_reshaped = np.reshape(my_arr, (2,4) , order = "F" )
# print(my_arr_reshaped)  # Traceback (most recent call last):
                    # File "c:\Users\pgold\MatsHub\Complete_2022_python_course\class_notes\python_scripting_libraries_OOPO\reshaping_modifying_and_Accessing.py", line 22, in <module>
                    #     my_arr_reshaped = np.reshape(my_arr, (2,4) , order = "F" )
                    # File "<__array_function__ internals>", line 180, in reshape
                    # File "C:\Users\pgold\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\numpy\core\fromnumeric.py", line 298, in reshape
                    #     return _wrapfunc(a, 'reshape', newshape, order=order)
                    # File "C:\Users\pgold\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\numpy\core\fromnumeric.py", line 57, in _wrapfunc
                    #     return bound(*args, **kwds)
                    # ValueError: cannot reshape array of size 20 into shape (2,4)



my_list = list(my_arr)
my_list[1] = 5
my_arr[1] = 6
print(my_list[1])  # 5
print(my_arr[1])  # 6

my_list_reshaped = list(my_arr_reshaped)
print(my_arr_reshaped[0,1])  # 5
print(my_list_reshaped[0][1])  # Traceback (most recent call last):
                            # File "c:\Users\pgold\MatsHub\Complete_2022_python_course\class_notes\python_scripting_libraries_OOPO\reshaping_modifying_and_Accessing.py", line 43, in <module>
                            #     print(my_list_reshaped[0,1])
                            # NameError: name 'my_list_reshaped' is not defined. Did you mean: 'my_arr_reshaped'?
print(my_arr_reshaped[0][1])  # 5






