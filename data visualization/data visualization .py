#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np
import requests as rs
import json as js
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[35]:


response=rs.get("https://raw.githubusercontent.com/theand9/data-viz-challenge/master/data.json")
job=js.loads(response.text)


# In[36]:


job=js.dumps(job['data'])


# In[37]:


df=pd.read_json(job)


# In[38]:


df.head()


# In[39]:


lc=pd.json_normalize(df['location'])
lc


# In[40]:


df=pd.concat([df.drop('location',axis=1), lc], axis=1)
df.head()


# In[41]:


for x in df:
    print(x,' - ',df[x].value_counts().sum(),end='\n')


# In[42]:


df.drop(['latitude','longitude','client_time','marital_status','device','zip_code'], axis=1, inplace=True)
df.head()


# In[43]:


df['event_name'].value_counts()


# In[44]:


a=df[(df['category']=='Sports') | (df['category']=='Environment')]


# In[45]:


a.shape


# In[46]:


a['event_name'].value_counts().plot.bar()


# In[47]:


a['session_id'].nunique()


# In[48]:


a[a['event_name']=='Fund Project'].session_id.nunique()


# In[58]:


plt.hist(a[a['event_name']=='Fund Project'].groupby('session_id').sum().amount, bins=50)


# In[59]:


a[a['event_name']=='Fund Project'].groupby(['session_id','gender']).sum()


# In[60]:


b=a[a['event_name']=='Fund Project']


# In[61]:


b.groupby('gender').mean().plot.bar()


# In[62]:


a.groupby(['event_name','gender']).count().category.plot.bar(x='distribution')


# In[63]:


b.groupby('age').mean().plot.bar()


# In[64]:


a.groupby(['event_name','age']).count().category.plot.bar()


# In[65]:


b.groupby(['state']).sum()


# In[ ]:




