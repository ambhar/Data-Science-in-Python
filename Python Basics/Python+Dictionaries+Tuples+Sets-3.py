
# coding: utf-8

# Dictionaries i.e key value pairs

# In[1]:

info = {'name':'amo','age':24}
print(info['name'])


# Lists inside Dictionaries

# In[3]:

info = {'name':'amo','age':24, 'marks':[20,25,30]}
print(info['marks'][0])


# Dictionary inside Dictionary

# In[5]:

info = {'name':'amo','info':{'address':['Miami','Newyork'],'phone':100}}
print(info['info']['address'][1])


# Tuples - similar to lists but instead of square bracketts we have ()

# In[7]:

tuple = (1,2,3)
print(tuple[1]) #Same as list


# Tuples are immutable, lists are mutable

# In[ ]:

tuple[0] = 10 # error as tuple is immutable, value at 0 index cant be changed


# Sets defined by unique elements

# In[9]:

s = {1,1,2,23,3,3,3}


# In[10]:

set([2,2,2,2,2,3,2,2,2,3,3,4,4,4]) # returns dictionary of unique elements


# In[ ]:

add element to a Set


# In[16]:

s = {1,2,2,3}
s.add(5)
print(s)

