
# coding: utf-8

# For Loops

# In[2]:

items = [1,2,3,4,5]
for item in items: #item can be named as anything here
    print(item)


# While Loop

# In[7]:

i = 1
while i < 2:
    print(i)
    # i+1 This makes infinite loop as value of i is not updating
    i = i+1


# Range function

# In[8]:

for item in range(2,4): # 4 is excluded
    print(item)


# List Comprehension

# In[9]:

x = [1,2,3,4]
y = []

for item in x:
    y.append(item ** 3)
print(y)


# The above code we can convert to List Comprehension code

# In[11]:

y = [item ** 3 for item in x] # List Comprehension
print(y)


# Python Functions 

# In[12]:

def name_of_function(): # function defined using keyword def
    print("python")
    
name_of_function()


# In[17]:

def name_of_function(name = 'default'): # function defined using keyword def
    print("Hello, " + name)
    
name_of_function('Python')


# Built IN MAP function

# In[25]:

def twice(var):
    return var * 2
numbers = [2,4,6]
map(twice, numbers) # returns memory address for the map


# In[26]:

list(map(twice, numbers))


# Lamba Representation for function or Anonymous Function

# In[27]:

def twice(var): return var * 2
new = lambda var: var * 2 # Lambda representation removed keywords def, return
new(5)


# In[28]:

list(map(lambda var: var * 2, numbers)) # lambda representation inside Map function


# Built IN Filter function

# In[30]:

list(filter(lambda num : num % 2 ==0, [2,3,4,5,6])) # filter out even numbers from a list


# In[ ]:

Some Built IN Functions lower, upper, upper


# In[33]:

str = "python is great"
str.lower() # all lower cases
str.upper() # all upper cases
str.split() # by default splits on white spaces, can add parameter to split based on that


# Some more functions

# In[34]:

mylist = [1,2,3,4]
mylist.pop() # gives last item of list and delete from mylist


# In[36]:

mylist.pop(0) # pops at index 0


# IN operator 

# In[37]:

2 in mylist # returns True


# In[38]:

lt = [(1,2), (2,3), (6,7)] # list of tuples


# In[39]:

lt[0][0] # prints 1


# Tuple Unpacking

# In[41]:

for (a,b) in lt: # Tuple Unpacking inside a list
    print(a) # prints 1,2,6
    print(b) # prints 2,3,7

