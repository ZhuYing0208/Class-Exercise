
# coding: utf-8

# In[1]:


2+8


# In[2]:


2.0+8.0


# In[3]:


2.0+8


# In[4]:


a=6
a


# In[5]:


s="Hello Zoey"
s


# In[9]:


s='''Hello
zoey'''
print(s)


# In[11]:


s="I"+"love"+"u"
s


# In[12]:


s="I love u"
s.split()


# In[13]:


s[0]


# In[18]:


s[-3]


# In[19]:


s[0:3]


# In[20]:


len(s)


# In[21]:


a =[2013,2,8,'with','u']
a


# In[23]:


a+a


# In[24]:


a[4]


# In[25]:


len(a)


# In[26]:


a.append("love")


# In[27]:


a


# In[30]:


i={2,8,13}
i


# In[31]:


len(i)


# In[32]:


i.add(2018)
i


# In[34]:


b={2,12,28,1996}
i&b


# In[35]:


i|b


# In[36]:


i-b


# In[38]:


i^b


# In[39]:


d={'boy':2,'girl':6}
d


# In[40]:


len(d)


# In[41]:


d["boy"]


# In[42]:


d["girl"]=5


# In[43]:


d


# In[44]:


d["woman"]=3
d


# In[45]:


d.keys()


# In[47]:


d.values()


# In[48]:


d.items()


# In[50]:


from numpy import array
a=array([2,8,2013])
a


# In[52]:


a+5


# In[53]:


a+a


# In[75]:


line = '2 8 20 13'
fields = line.split()
fields


# In[76]:


total = 0
for field in fields:
    total += int(field)
total


# In[77]:


cd~


# In[81]:


f=open('data.txt','w')
f.write('2 3 4 5\n')
f.write('6 7 8 9\n')
f.close()


# In[82]:


f=open('data.txt')
data=[]
for line in f:
    data.append([int(field) for field in line.split()])
f.close
data


# In[85]:


for row in data:
    print(row)


# In[87]:


import os
os.remove('data.txt')


# In[88]:


def zy(a,b,c):
    a=b**2+c
    return a
zy(a,2,8)


# In[106]:


class Student(object):
    def __init__(stu,first, last, age,number):
        stu.first= first
        stu.last= last
        stu.age= age
        stu.number=number
    def full_name(stu):
        return stu.first+ ' ' + stu.last


# In[107]:


student=Student('Zoey','Zhu','18','281440')


# In[91]:


student.first_name


# In[92]:


student.full_name()


# In[93]:


student.first='Ying'


# In[94]:


student.full_name()


# In[95]:


"call"*4


# In[101]:


numbers="12345"
s=' '
s.join(numbers)


# In[102]:


s='、'
s.join(numbers)


# In[108]:


s="I love u"
s.replace('u','zyp')


# In[109]:


s


# In[114]:


print (s.upper())
print (s)

