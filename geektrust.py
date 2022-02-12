#!/usr/bin/env python
# coding: utf-8

# ## Import Libraries

# In[16]:


import numpy as np
import pandas as pd


# ## Create a Dataframe

# In[17]:


train_A = pd.DataFrame({"station": ['CHENNAI (CHN)', 'SALEM (SLM)', 'BANGALORE (BLR)', 'KURNOOL (KRN)', 'HYDERABAD (HYB)','NAGPUR (NGP)',
                         'ITARSI (ITJ)', 'BHOPAL (BPL)', 'AGRA (AGA)', 'NEW DELHI (NDL)'], 
                        "distance1" : [0,350,550,900,1200,1600,1900,2000,2500,2700]})
display(train_A)

train_B = pd.DataFrame({"station": ['TRIVANDRUM (TVC)', 'SHORANUR (SRR)', 'MANGALORE (MAQ)', 'MADGAON (MAO)', 'PUNE (PNE)','HYDERABAD (HYB)',
                        'NAGPUR (NGP)', 'ITARSI (ITJ)', 'BHOPAL (BPL)', 'PATNA (PTA)', 'NEW JALPAIGURI (NJP)', 'GUWAHATI (GHY)'], 
                        "distance2" : [0,300,600,1000,1400,2000,2400,2700,2800,3800,4200,4700]})
display(train_B)

## order of bogies for train A while arriving at Hyderabad

station_distance1 = train_A[train_A['distance1'] < 1200].index
train_A.drop(station_distance1, inplace = True)
display(train_A)


## order of bogies for train B while arriving at Hyderabad

station_distance2 = train_B[train_B['distance2'] < 2000].index
train_B.drop(station_distance2, inplace = True)
display(train_B)

## order of bogies for train AB (merged train) while departing from Hyderabad

train_AB = pd.merge(left=train_A, right=train_B, left_on = "station",right_on = "station", how = "outer")
train_AB.sort_values("station", inplace = False)
bool_series = train_AB["station"].duplicated()
train_AB


# ## Extract Common Stations

# In[19]:


train_AB = pd.merge(train_A, train_B, on = "station", how = "inner")
train_AB['distance_diff'] = [0,400,700,800]
print(train_AB)


# In[ ]:




