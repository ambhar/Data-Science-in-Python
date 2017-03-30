
# coding: utf-8

# # Numpy Array Indexing and Selection

# In[2]:

import numpy as np


# In[4]:

arr = np.arange(0,10) # 0 - 9


# In[5]:

arr[8] # gives 8


# In[11]:

arr[1:3] # gives array([1, 2])
arr[1:3] = 10 
arr # index 1 and 2 values will be 10 now


# In[19]:

slice_arr = arr[1:3]
slice_arr[:] = 10 # all values of slice array are replaced by 10
slice_arr  # o/p = array([10, 10])
arr # o/p = array([ 0, 10, 10,  3,  4,  5,  6,  7,  8,  9])

# the slice_arr value got changed inside the main array. That means slice_arr is just a view or reference of a part of arr, but it belongs to the main array.



# In[20]:

arr.copy() # this creates a separate copy for us


# In[33]:

arr = np.arange(25)
arr = arr.reshape(5,5)
"""

O/P

array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24]])
       
"""

arr[:2,:3]
"""
row upto 2, column upto 3
o/p
array([[0, 1, 2],
       [5, 6, 7]])
"""
arr[:3,3:]

"""
o/p
array([[ 3,  4],
       [ 8,  9],
       [13, 14]])
"""


# # CONDITIONAL SELECTIONS

# In[34]:

arr = np.arange(1,10)


# In[35]:

arr > 3 # o/p Returns false where value less than 3, - array([False, False, False,  True,  True,  True,  True,  True,  True], dtype=bool)


# In[36]:

arr[arr>5] # returns values of arr which are greater than 5 - array([6, 7, 8, 9])


# In[ ]:



