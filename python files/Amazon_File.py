# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 00:37:02 2018

@author: gupta
"""


# -*- coding: utf-8 -*-


import pandas as pd 
amazon_file= pd.read_csv('C:\\Users\\gupta\\.spyder-py3\\amazon2.csv')
print(amazon_file)

# to lower case

amazon_file['review']= amazon_file['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
amazon_file['review'].head()

# exract emoji 

import emot

amazon_list =amazon_file['review']
l=[]
for i in range(len(amazon_list)):
    #print (emot.emoji(reviewlist[i]).get("value","none"))
    x= emot.emoji(amazon_list[i]).get("mean","none")
    l.append(x)   
    
amazon_file['emoji']=l

emoji_file1= pd.read_csv('C:\\Users\\gupta\\.spyder-py3\\amazon_emotions.csv')
emoji_file1['emoji'] = emoji_file1['emoji'].str.replace('[^\w\s]','')
emoji_file1['emoji'].tail()
# punctuation removal

amazon_file['review'] = amazon_file['review'].str.replace('[^\w\s]','')
amazon_file['review'].tail()

# stop words removal

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop = set(stopwords.words('english'))
amazon_file['review'] = amazon_file['review'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
amazon_file['review'].head()

# number removal

amazon_file['review'] = amazon_file['review'].str.replace('\d+', '')
amazon_file['review'].head()

#replace words

amazon_file.Review = amazon_file.Review.str.replace('app', 'application')
amazon_file.Review = amazon_file.Review.str.replace('specify', 'spotify')

# Lemmatization

import nltk
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

lemmatizer = WordNetLemmatizer()

amazon_file['review']= amazon_file['review'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word,'n')for word in x.split()]))
amazon_file['review']= amazon_file['review'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word,'v')for word in x.split()]))
print(amazon_file['review'])

# spelling correction
from autocorrect import spell 
amazon_file['review']= amazon_file['review'].apply(lambda x: " ".join([spell(i) for i in x.split()]))



