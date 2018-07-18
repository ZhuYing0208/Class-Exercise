
# coding: utf-8

# In[4]:


from nltk.util import ngrams
a = "add domain with authentication for conference focus user".split(' ')
b = ngrams(a,2)
for i in b:
    print (i)


# In[2]:


import datetime as dt


# In[3]:


d1=dt.date(2018,5,15)


# In[4]:


d1


# In[5]:


print(d1)


# In[6]:


print(d1.strftime('%m/%d/%y'))


# In[7]:


dt.datetime.now()


# In[11]:


print(dt.datetime.now().strftime('%m/%d/%y %H-%M-%S'))


# In[12]:


def square(a):
    return a*a


# In[13]:


a=[1,3,5]
b=map(square,a)


# In[14]:


b


# In[15]:


b=[square(i) for i in a]


# In[16]:


b


# In[17]:


lambda x:x*x


# In[18]:


def square(x):return x*x


# In[19]:


import numpy


# In[20]:


numpy.pi


# In[21]:


import csv


# In[22]:


data=[(1,3,5,5,7),(1,2,5,4,7),(1,2,3,4,5)]


# In[24]:


with open('o.csv','w')as f:
    w=csv.writer(f)
    w.writerows(data)


# In[25]:


w1.witerow(('a','b','c'))


# In[26]:


data1=[]
f=open('o.csv','r')
r=csv.reader(f)
for row in r:
    print(row)

