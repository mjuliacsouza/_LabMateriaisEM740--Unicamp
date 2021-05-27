#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import seaborn as srn
import statistics  as sts


# In[11]:


liga2024EN_N = pd.read_csv("liga2024envnatural.csv",sep=";")


# In[24]:


print(liga2024EN_N)


# In[12]:


liga2024EA_N = pd.read_csv("liga2024envartificial.csv",sep=";")


# In[20]:


liga2024EA_N


# In[13]:


liga2024EA_N = pd.read_csv("liga6351envnatural.csv",sep=";")


# In[21]:


liga2024EA_N


# In[14]:


liga6351EA_N = pd.read_csv("liga6351envarticial.csv",sep=";")


# In[18]:


liga6351EA_N

