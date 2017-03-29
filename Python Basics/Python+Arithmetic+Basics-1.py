
# coding: utf-8

# Addition of integers

# In[8]:

1 + 3


# multiply of integers

# In[3]:

1 * 3


# exponents

# In[6]:

2 ** 2 


# division

# In[5]:

1 / 2 


# Modulus operator

# In[10]:

11 % 2


# Variables

# In[11]:

x = 10
y = 20
x + y


# Print Formatting to add variables inside a print statement. Variables are in order

# In[12]:

age = 20
name = 'amo'
print('My name is {} and age is {}'.format(name, age))


# Print Formatting to add variables inside a print statement. Variables can be in any order

# In[13]:

age = 20
name = 'amo'
print('My name is {name} and age is {age}'.format(name=name, age=age))


# string as array

# In[14]:

name = 'amo'
print(name[2]) # index 2


# Colon Notation (At index and beyond)

# In[15]:

name = 'freelancer'
print(name[2:]) # index 2 and beyond


# In[17]:

name = 'freelancer'
print(name[2:5]) # 3rd character i.e index 2 to 4 (excluded 5)


# In[18]:

name = 'freelancer'
print(name[:5]) # characters upto index 5, excluding 5


# Python Lists

# In[ ]:

['a','b','c']


# In[ ]:

[2,4,55] #Integer List


# In[ ]:

Append to list


# In[19]:

items = ['a','b']
items.append('c')
print(items)


# add at index

# In[20]:

items = ['a','b']
items[1]='x'
print(items)


# List inside List

# In[23]:

items = ['a','b',[1,2]]

print(items[2][1]) # 1st index of list at index 2 of list items

