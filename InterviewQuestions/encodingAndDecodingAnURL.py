
# coding: utf-8

# In[19]:


#Encode and Decode URL
#Encoding items into a url. An URL will have 6 components that make a string into a valid URL.

import urllib
params = {"session_id":"1234","input":"Hello World"}


# In[20]:


#This will take in params and create a url
url_params = urllib.parse.urlencode(params)


# In[21]:


print (url_params)


# In[23]:


#Decoding a URL
from urllib.parse import urlparse

#This will take in any URL and split the input into 6 basic URL components.
url_params = "https://weather.com/weather/hourbyhour/l/USNJ0612:1:US"
params_dict = urlparse(url_params)
print(params_dict)

