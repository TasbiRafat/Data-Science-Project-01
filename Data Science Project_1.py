#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv('COVID-19 BD Dataset-15 april.csv')
print(data)


# In[4]:


data.head()


# In[5]:


data.columns


# In[6]:


data.tail()


# In[7]:


data.describe()


# In[8]:


data.isnull().sum()


# In[9]:


sns.relplot(x="Total confirmed cases", y = "Total recovered", data = data)


# In[12]:


sns.relplot(x="Total confirmed cases", y = "Total deaths", hue='Total recovered', data = data)


# In[13]:


sns.pairplot(data)


# In[15]:


sns.relplot(x="Total confirmed cases", y = "Total deaths", kind='line', data = data)


# In[16]:


sns.catplot(x="Total confirmed cases", y = "Total deaths", data = data)


# In[ ]:
