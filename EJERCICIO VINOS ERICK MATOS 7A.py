#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plot
get_ipython().magic('matplotlib inline')


# In[2]:


ls


# In[3]:


ls


# In[4]:


df = pd.read_csv("winequality-red.csv",encoding='latin1')


# In[10]:


df.describe()


# In[6]:


df.columns


# In[28]:


sns.distplot(df.pH)


# In[8]:


sns.distplot(df.quality)


# In[ ]:




