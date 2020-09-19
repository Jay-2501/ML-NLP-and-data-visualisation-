#!/usr/bin/env python
# coding: utf-8

# In[2]:


import string 
import sys 


# In[3]:


def read_file(filename):  
      
    try: 
        with open(filename, 'r') as f: 
            data = f.read() 
        return data 
    except IOError: 
        print("Error opening or reading input file: ", filename) 
        sys.exit()
    


# In[4]:



translation_table = str.maketrans(string.punctuation+string.ascii_uppercase, 
                                     " "*len(string.punctuation)+string.ascii_lowercase) 
       


# In[5]:


def calculate_frequency(word_list):  
    vector = {} 
      
    for word in word_list: 
          
        if word in vector: 
            vector[word] += 1
              
        else: 
            vector[word] = 1
              
    return vector


# In[6]:


def word_frequencies(filename):  
      
    line_list = read_file(filename) 
    word_list = line_list.translate(translation_table).split() 
      
    return calculate_frequency(word_list)  


# In[7]:


def dot_product(vector1, vector2):  
    Sum = 0.0
      
    for key in vector1: 
        if key in vector2: 
            Sum += (vector1[key] * vector2[key]) 
              
    return Sum


# In[13]:


def cos(vector1, vector2):    
    adotb = dot_product(vector1, vector2
    modab = (dot_product(vector1, vector1)*dot_product(vector2, vector2))**0.5                   
      
    return adotb / modab


# In[9]:


def SimilarityScore(file1, file2): 
      
    file1_vector = word_frequencies(file1) 
    file2_vector = word_frequencies(file2) 
    similarity = cos(file1_vector, file2_vector) 
      
    print("The cosine similarity of the given documents is: % 0.4f "% similarity) 


# In[10]:


SimilarityScore('r.txt', 'r.txt') 


# In[ ]:




