

# ### A list of n integer values 

# In[60]:


price =[300, 600, 900, 1000, 1500, 1800, 2100]

print(price)


# ### Add an item in to the list (using function)

# In[61]:


price.append(2400)

print(price) 

price.extend(price)

print(price)

print(price[3])

price.insert(3,1200)

print(price)


# ### Delete (using function)

# In[62]:



del price[0]
print(price)

price.pop()
print(price)

price.remove(900)
print(price)


# ### Store the Smallest number from the list to a variable
# ### Store the Largest number from the list to a variable

# In[63]:


Low = min(price)

High = max(price)

print(Low)

print(High)


# ### Create a tuple and print the reverse of the created tuple

# In[64]:


my_info = ("Ketan",8177899637,21,"ETC Engineer")
print(my_info)


# In[70]:


my_info = tuple(reversed(my_info))
print(my_info)


# ### Create a tuple and convert tuple into list

# In[71]:


Tuple = (22,'K',81,91,61,71,'e','t') 
Tuple = list(Tuple)
print(Tuple)


# In[ ]:




