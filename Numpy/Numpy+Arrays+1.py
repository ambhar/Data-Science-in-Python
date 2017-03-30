
# coding: utf-8

# # Numpy Arrays

# In[3]:

list = [1,2,3]


# In[2]:

import numpy as np


# In[4]:

arr = np.array(list) # numpy array array([1, 2, 3]) one dimensional


# In[5]:

matrix = [[1,2,3], [4,5,6], [7,8,9]]
np.array(matrix) """
Output

array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
       
"""


# In[6]:

np.arange(0,10) # output = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[7]:

np.arange(0,10,3) # output = array([0, 3, 6, 9])
# here stepsize 3 is added, so at every third number array element is added


# In[10]:

np.zeros(3) # 1 D array for zeros

np.zeros((3,3))
"""
2D array of zeros
array([[ 0.,  0.,  0.],
       [ 0.,  0.,  0.],
       [ 0.,  0.,  0.]])
       
Similarly for np.ones
"""


# In[12]:

np.linspace(0,5,10) # in the range 0-5, get 10 evenly spaced values

"""
o/p

array([ 0.        ,  0.55555556,  1.11111111,  1.66666667,  2.22222222,
        2.77777778,  3.33333333,  3.88888889,  4.44444444,  5.        ])
        
"""


# In[13]:

# Identity matrix in numpy

np.eye(5)

"""
o/p
array([[ 1.,  0.,  0.,  0.,  0.],
       [ 0.,  1.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  0.,  1.]])
       
"""


# In[14]:

# array populating random samples of uniform distribution from 0-1
np.random.rand(5) # o/p array([ 0.51945737,  0.33365626,  0.33747399,  0.75010991,  0.20829327])


# In[15]:

np.random.rand(5,5) # gives 2D


# In[16]:

np.random.randn(4) # will return standard normal distribution centered around 0
np.random.randn(4,4) # 2D


# In[23]:

np.random.randint(1,100) # 100 is exclusive
ranarray = np.random.randint(1,100, 10) # 10 random numbers 1-99


# In[30]:

arr = np.arange(0,25)
arr = arr.reshape(5,5) # 1D to 2D, elements size should remain same


# In[25]:

ranarray.max() # max value in array
ranarray.min() # min value in array


# In[26]:

ranarray.argmin() # min value index in array


# In[33]:

arr.shape # o/p = (5,5) gives shape of array
arr.dtype # o/p = dtype('int64'), gives datatype of array items


# In[ ]:



