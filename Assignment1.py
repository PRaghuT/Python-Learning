#!/usr/bin/env python
# coding: utf-8

# In[13]:


#1. Install Jupyter notebook and run the first program and share the screenshot of the output.
a = 3
b = 4
print(a+b)


# In[14]:


""" 2 .Write a program which will find all such numbers which are divisible by 7 but are not a multiple
of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
comma-separated sequence on a single line."""


for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i,end = ",")


# In[15]:


"""3. Write a Python program to accept the user's first and last name and then getting them printed in
the the reverse order with a space between first name and last name."""

First_Name = input("Enter First Name:")
Last_Name = input("Enter Last Name:")
print(First_Name[-1::-1]+" "+Last_Name[-1::-1])


# In[20]:


"""4. Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r
3"""
import math
d = 12
r = d/2
Volume = (4/3)*math.pi*r**3
print(Volume)


# In[23]:


"""5. Write a program which accepts a sequence of comma-separated numbers from console and
generate a list."""

Numbers = input("Enter_Comma_Sep_numbers:")
L = Numbers.split(",")
print(L)


# In[27]:


"""6. Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

for i in range(5):
    print("*"*i)
for j in range(5,0,-1):
    print("*"*j)


# In[31]:


"""7. Write a Python program to reverse a word after accepting the input from the user."""
Word = input("Enter a word to Reverse: ")
print(Word[-1::-1])


# In[71]:


"""8.Write a Python Program to print the given string in the format specified in the sample output.
WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
its citizens
Sample Output:
WE, THE PEOPLE OF INDIA,
    having solemnly resolved to constitute India into a SOVEREIGN, !
        SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
        and to secure to all its citizens"""

String = "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens"

a = String.split("having")
b = a[1].split("SOVEREIGN,")
print(String.split("having")[0])
print("\t""having"+str(a[1].split("SOCIALIST")[0])+"!")
print("\t\t"+str(b[1].split("and")[0]))
print("\t\t"+str(b[1].split("REPUBLIC")[1]))



# In[ ]:




