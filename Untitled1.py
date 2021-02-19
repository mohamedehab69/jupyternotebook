#!/usr/bin/env python
# coding: utf-8

# In[2]:


def perimeter_of_Rectangle(length, width):
    return 2 * (length + width)

length = float(input('Please Enter the Length of a Triangle: '))
width = float(input('Please Enter the Width of a Triangle: '))

# calculate the perimeter
perimeter = perimeter_of_Rectangle(length, width)
print("Perimeter of a Rectangle using", length, "and", width, " = ", perimeter)


# In[ ]:




