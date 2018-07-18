
# coding: utf-8

# In[3]:


para = "Hello World. It's good to see you. Thanks for buying this book."


# In[14]:


import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize


# In[15]:


sent_tokenize(para)


# In[17]:


from nltk.tokenize import word_tokenize


# In[18]:


word_tokenize('Hello World.')


# In[19]:


from nltk.tokenize import TreebankWordTokenizer 


# In[21]:


tokenizer = TreebankWordTokenizer() 


# In[22]:


tokenizer.tokenize('Hello World.') 


# In[23]:


import nltk 


# In[24]:


text = "Hello. Isn't this fun?" 


# In[26]:


pattern = r"\w+|[^\w\s]+"


# In[27]:


print (nltk.tokenize.regexp_tokenize(text, pattern) )


# In[28]:


from nltk.tokenize import RegexpTokenizer 


# In[29]:


tokenizer = RegexpTokenizer("[\w']+") 


# In[30]:


tokenizer.tokenize("Can't is a contraction.") 


# In[31]:


from nltk.tokenize import PunktSentenceTokenizer 


# In[35]:


from nltk.corpus import webtext 
import nltk
nltk.download('webtext')


# In[37]:


text = webtext.raw('overheard.txt') 


# In[38]:


sent_tokenizer = PunktSentenceTokenizer(text) 


# In[39]:


sents1 = sent_tokenizer.tokenize(text) 


# In[40]:


from nltk.tokenize import sent_tokenize 


# In[41]:


sents2 = sent_tokenize(text) 


# In[42]:


sents2[0] 


# In[45]:


from nltk.corpus import stopwords 
import nltk
nltk.download('stopwords')
  


# In[47]:


english_stops = set(stopwords.words('english')) 


# In[48]:


words = ["Can't", 'is', 'a', 'contraction'] 


# In[49]:


[word for word in words if word not in english_stops] 


# In[52]:


from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')
  


# In[53]:


syn = wordnet.synsets('cookbook')[0] 


# In[54]:


syn.name() 


# In[55]:


syn.definition() 


# In[56]:


from nltk.corpus import wordnet 


# In[57]:


syn = wordnet.synsets('motorcar')[0] 


# In[58]:


syn.name 


# In[59]:


from nltk.corpus import wordnet as wn 


# In[60]:


wn.synsets("motorcar")


# In[61]:


from nltk.corpus import wordnet as wn 


# In[62]:


motorcar = wn.synset('car.n.01') 


# In[63]:


types_of_motorcar = motorcar.hyponyms()


# In[64]:


types_of_motorcar 


# In[65]:


from nltk.corpus import wordnet as wn 


# In[66]:


wn.synset('tree.n.01').part_meronyms() 


# In[67]:


wn.lemma('beautiful.a.01.beautiful').antonyms() 


# In[68]:


dir(wn.synset('beautiful.a.01')) 


# In[69]:


from nltk.corpus import wordnet 


# In[70]:


syn = wordnet.synsets('motorcar')[0] 


# In[71]:


syn.pos() 


# In[72]:


from nltk.corpus import wordnet as wn 


# In[73]:


wn.synset('car.n.01').lemma_names()


# In[74]:


a = wn.synset('car.n.01').lemma_names() 


# In[75]:


print(a)


# In[76]:


wn.synset('car.n.01').definition () 


# In[77]:


from nltk.corpus import wordnet as wn 


# In[78]:


right = wn.synset('right_whale.n.01') 
minke = wn.synset('minke_whale.n.01') 
right.path_similarity(minke) 

