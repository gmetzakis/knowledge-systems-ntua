#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def is_specified(val):
    unspecified_indicators = ['\\N']
    return val not in unspecified_indicators and val is not None
  
uri_base = 'http://www.ex.org/gmetz/ontology/'