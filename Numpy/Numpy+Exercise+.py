
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[4]:

import numpy as np


# #### Create an array of 10 zeros 

# In[6]:

np.zeros(10)


# #### Create an array of 10 ones

# In[8]:

np.ones(10)


# #### Create an array of 10 fives

# In[10]:

np.ones(10)*5


# In[ ]:




# #### Create an array of the integers from 10 to 50

# In[11]:

np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[12]:

np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[19]:

arr = np.arange(0,9).reshape(3,3)


# In[20]:

arr


# #### Create a 3x3 identity matrix

# In[21]:

np.eye(3,3)


# #### Use NumPy to generate a random number between 0 and 1

# In[23]:

np.random.rand()


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[24]:

np.random.randn(25)


# #### Create the following matrix:

# In[28]:

np.arange(0.01,1.01,0.01)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[31]:

np.linspace(0,1,20)


# In[ ]:




# In[ ]:




# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[38]:

mat = np.arange(1,26).reshape(5,5)
mat


# In[37]:

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat = np.arange(1,26).reshape(5,5)
mat
mat[2:,1:]


# In[40]:




# In[38]:

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[3,4]


# In[41]:




# In[48]:

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[:3,1:2]


# In[42]:




# In[31]:

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[50]:

mat[4]


# In[51]:

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[3:]


# In[49]:




# ### Now do the following

# #### Get the sum of all the values in mat

# In[53]:

np.sum(mat)


# #### Get the standard deviation of the values in mat

# In[54]:

np.std(mat)


# #### Get the sum of all the columns in mat

# In[56]:

mat.sum(axis=0)


# # Great Job!
