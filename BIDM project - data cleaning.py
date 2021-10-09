#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


pd.read_csv('ridership data.csv')


# In[4]:


rough_data_ridership = pd.read_csv('ridership data.csv')
print(rough_data_ridership)


# In[5]:


ridership_data = rough_data_ridership.rename(columns = {'route':'Route Code', 
                                                        'ridership_route_code':'Ridership Code', 
                                                        'route_full_name': 'Route Name', 
                                                        'current_garage': 'Garage', 
                                                        'mode': 'Mode', 
                                                        'month_start': 'Date', 
                                                        'year_month': 'Month_old', 
                                                        'day_type':'Day', 
                                                        'avg_riders':'Average Rider', 
                                                        'day_count': 'Count of Days'})
print(ridership_data)
len(ridership_data)


# In[6]:


ridership_data.drop(columns =['Ridership Code'], inplace = True)
print(ridership_data)
len(ridership_data)


# In[7]:


is_NaN = ridership_data.isnull()
row_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = ridership_data[row_has_NaN]
print(rows_with_NaN)


# In[8]:


ridership_data[["Year", "Month", "Day #"]] = ridership_data["Date"].str.split("-", expand = True)
print(ridership_data)


# In[9]:


ridership_data.drop(columns =['Month_old'], inplace = True)


# In[10]:


print(ridership_data)


# In[11]:


#removing NaN values

ridership_data.dropna(inplace = True)
ridership_data.reset_index(inplace = True)
len(ridership_data)
print(ridership_data)


# In[12]:


#Monthly schedule 


pd.read_csv('monthly_schedule data.csv')


# In[14]:


rough_data_schedule = pd.read_csv('monthly_schedule data.csv')
print(rough_data_schedule)


# In[21]:


schedule_data = rough_data_schedule.rename(columns = {'PickID':'ID', 
                                                        'dateKey':'sch_date', 
                                                        'Route': 'Sch_Route', 
                                                        'RouteCode': 'Route Code', 
                                                        'Daily.Trip.Dist': 'Daily trip distance', 
                                                        'Daily.Trip.Count': 'Daily trip count', 
                                                        'Day.Type.Join': 'Sch_Day', 
                                                        'Route_Full_Name':'Sch_Route Name', 
                                                        'Current_Garage': 'Sch_Garage', 
                                                        'Mode': 'Sch_Mode'})
print(schedule_data)
len(schedule_data)
#Note - check join on route & route code 


# In[22]:


is_NaN2 = schedule_data.isnull()
row_has_NaN2 = is_NaN2.any(axis=1)
row_with_NaN2 = schedule_data[row_has_NaN2]
print(row_with_NaN2)

#No null values


# In[34]:


combined_df = pd.merge(schedule_data, ridership_data, on=['Route Code'])
print(combined_df)
len(combined_df)


# In[35]:


combined_df.drop_duplicates(inplace = True)
print(len(combined_df))


# In[27]:


schedule_data.to_csv("schedule_data.csv", sep = ',')
ridership_data.to_csv("ridership_data.csv", sep = ',')


# In[33]:


new_data = pd.concat(ridership_data, schedule_data)
print(new_data)


# In[ ]:




