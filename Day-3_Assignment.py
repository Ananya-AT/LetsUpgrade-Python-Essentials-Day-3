#!/usr/bin/env python
# coding: utf-8

# # Question-1

# In[7]:


alt=int(input("Enter the height"))
if alt <= 1000:
    print("safe to land")
elif alt>1000 and alt<5000:
    print("Bring down to 1000")
else:
    print("Turn around")


# # Question-2

# In[13]:


lower=1
upper=200
print("prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num>1:
        for i in range(2, num):
            if(num%i)==0:
                break
            else:
                print(num)


# In[ ]:




