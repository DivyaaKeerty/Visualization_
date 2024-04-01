#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


salesdata = pd.read_csv(r"C:\Users\Public\Python CaseStudies\PYHTON CS4\SalesData.csv")
salesdata.head(2)


# ### Compare Sales by region for 2016 with 2015 using bar chart ###

# In[3]:


region_sales = salesdata.groupby("Region")["Sales2015","Sales2016"].sum()


# In[4]:


region_sales


# In[5]:


plt.figure(figsize=(6,3))
region_sales.plot(kind="bar",figsize=(,4))
plt.ylabel('Sales')
plt.title("Sales by region for 2016 with 2015")
plt.show()


# In[ ]:





# ### what are the contributing factors to the sales for each region in 2016. Visualize it using a Pie Chart ###

# In[6]:


salesdata.head()


# In[7]:


sales_pie = salesdata.groupby("Region")["Sales2016"].sum()


# In[8]:


sales_pie


# In[9]:


plt.pie(sales_pie,autopct="%1.0f%%",labels=["Central","East","West"],shadow=True,explode=[0.0,0.1,0.0],colors=['red', 'blue', 'yellow'])
plt.title("Contributing factors to the sales for each region in 2016")
plt.show()


# In[10]:


print("East region has contributed the maximum in 2016.")


# In[ ]:





# ###  Compare the total sales of 2015 and 2016 with respect to Region and Tiers

# In[11]:


sales_region_tier = salesdata.groupby(["Region","Tier"])['Sales2015','Sales2016'].sum()
sales_region_tier


# In[12]:


sales_region_tier.plot(kind="bar",figsize=(4,4))
plt.ylabel("Sales")
plt.title("Total sales of 2015 and 2016 with respect to Region and Tiers")
plt.show()


# In[13]:


sales_region_tier.plot(kind="barh",stacked=True,figsize=(4,4))
plt.xlabel("Sales")
plt.ylabel("Region/Tier")
plt.title("Total sales of 2015 and 2016 with respect to Region and Tiers")
plt.show()


# ### 4. In East region, which state registered a decline in 2016 as compared to 2015? ###

# In[14]:


sales_state = salesdata.groupby(['Region',"State"])['Sales2015','Sales2016'].sum()


# In[15]:


sales_state


# In[16]:


sales_east = sales_state.loc["East"]


# In[17]:


sales_east


# In[18]:


sales_east.plot(kind="bar",figsize=(6,3),width=0.8)
plt.ylabel("Sales")
plt.title("Sales comparison between 2015 and 2016 for East Region")
plt.show()


# In[ ]:





# ### In all the High tier, which Division saw a decline in number of units sold in 2016 comparedto 2015? ###

# In[19]:


salesdata.head(1)


# In[20]:


sales_division_tier =salesdata.groupby(["Tier","Division"])["Units2015","Units2016"].sum()


# In[21]:


sales_division_tier


# In[22]:


high_tier = sales_division_tier.loc["High"]


# In[23]:


high_tier


# In[24]:


high_tier.plot(kind="bar",figsize=(6,3),width=0.7)


# In[ ]:





# ### . Create a new column Qtr using numpy.where() or any suitable utility in the imported dataset. The Quarters are based on months and defined as -
# • Jan - Mar : Q1
# • Apr - Jun : Q2
# • Jul - Sep : Q3
# • Oct - Dec : Q4

# In[25]:


salesdata.head(2)


# In[26]:


month =salesdata["Month"]


# In[27]:


quarter = []
for x in month :
    if x in ["Jan","Feb","Mar"]:
        quarter.append("Q1")
    elif x in ["Apr","May","Jun"]:
        quarter.append("Q2")
    elif x in ["Jul","Aug","Sep"]:
        quarter.append("Q3")
    else:
        quarter.append("Q4")


# In[28]:


quarter


# In[29]:


salesdata["Qtr"]= pd.Series(quarter)


# In[30]:


salesdata


# ###  Compare Qtr wise sales in 2015 and 2016 in a bar plot

# In[31]:


qtr_sales = salesdata.groupby("Qtr")["Sales2015","Sales2016"].sum()


# In[32]:


qtr_sales


# In[33]:


qtr_sales.plot(kind="bar")
plt.ylabel("Sales")
plt.title("Quarter wise sales in 2015 and 2016")
plt.show()


# In[ ]:





# ### 8 . Determine the composition of Qtr wise sales in and 2016 with regards to all the Tiers in a pie chart.
#  (Draw 4 pie charts representing a Quarter for each Tier)

# In[34]:


qtr_pivot = salesdata.pivot_table(index='Qtr',columns='Tier',values='Sales2016')


# In[35]:


qtr_pivot


# In[36]:


plt.pie(x=qtr_pivot.loc["Q1",:],autopct="%1.0f%%",labels=["High","Low","Med","Out"],colors=['yellow', 'orange', 'red'])
plt.show()


# In[37]:


plt.pie(x=qtr_pivot.loc["Q2",:],autopct="%1.0f%%",labels=["High","Low","Med","Out"],colors=['yellow', 'orange', 'red'])
plt.show()


# In[38]:


plt.pie(x=qtr_pivot.loc["Q3",:],autopct="%1.0f%%",labels=["High","Low","Med","Out"],colors=['yellow', 'orange', 'red'])
plt.show()


# In[39]:


plt.pie(x=qtr_pivot.loc["Q4",:],autopct="%1.0f%%",labels=["High","Low","Med","Out"],colors=['yellow', 'orange', 'red'])
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




