#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus 
# the length of the lists can differ)

data = {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
       'Italy': [6, 8, 1, 7]}


# In[11]:


# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country

def total_registered_cases(data, countryname):
    print(sum(data[countryname]))
    
total_registered_cases(data, 'Spain')


# In[42]:


# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had

def total_registered_cases_per_country(data):
    new_dict = {k: sum(data[k]) for k in data.keys()}
    return new_dict
    
total_registered_cases_per_country(data)


# In[51]:


# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

def country_with_most_cases(data):
    new_dict = {k: sum(data[k]) for k in data.keys()}
    return max(new_dict, key = new_dict.get)

country_with_most_cases(data)


# In[ ]:




