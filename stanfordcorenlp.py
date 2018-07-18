
# coding: utf-8

# In[2]:


#coding: utf-8
# 引入库
from stanfordcorenlp import StanfordCoreNLP
# 用与英文处理的客户实例
nlp_en = StanfordCoreNLP('http://192.168.101.7', port=2002)   
# 用与中文处理的客户实例
nlp_cn = StanfordCoreNLP('http://192.168.101.7', port=2003)  
en_txt = "There are more public options, too. For example, in 2013, Chinese state media accused Jaguar Land Rover and Audi of overcharging buyers for car parts, which analysts viewed as part of a campaign to pressure those automakers to locate more manufacturing in China."
cn_txt = "还有更多的公开选择。比如，2013年，中国官方媒体指责捷豹路虎(Jaguar Land Rover)和奥迪(Audi)对汽车零部件的买家要价过高。分析师认为，那是在向这些汽车制造商施压，让它们把更多的制造工作搬到中国去。"


# In[12]:


nlp_en.word_tokenize(en_txt)
nlp_cn.word_tokenize(cn_txt)


# In[13]:


nlp_en.pos_tag(en_txt)
nlp_cn.pos_tag(cn_txt)


# In[14]:


nlp_en.ner(en_txt)
nlp_cn.ner(cn_txt)

