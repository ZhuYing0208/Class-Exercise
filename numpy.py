
# coding: utf-8

# In[1]:


from numpy import *


# In[3]:


a=[1,2,3,4,5]
a+2


# In[4]:


a=array(a)
a


# In[5]:


a+2


# In[6]:


b=[2,0,1,3,2]
a+b


# In[7]:


a[:3]


# In[10]:


a[:-3]


# In[11]:


a.shape


# In[22]:


a=array ([1,2,3,4,5,6])


# In[23]:


a.shape


# In[29]:


a.shape=2,3
a


# In[31]:


a=linspace(0,2*pi,21)
get_ipython().run_line_magic('precision', '3')
a


# In[32]:


b=sin(a)
b


# In[34]:


get_ipython().run_line_magic('matplotlib', 'inline')
plot(a,b)

