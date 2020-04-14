# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:57:31 2018

@author: gupta
"""


# -*- coding: utf-8 -*-


import pandas as pd 
pandora_file= pd.read_csv('C:\\Users\\gupta\\.spyder-py3\\Pandora.csv')
print(pandora_file)

# to lower case

pandora_file['Rev']= pandora_file['Rev'].apply(lambda x: " ".join(x.lower() for x in x.split()))
pandora_file['Rev'].head()

# exract emoji 

import emot

spotify_list =pandora_file['Rev']
l=[]
for i in range(len(spotify_list)):
    #print (emot.emoji(Revlist[i]).get("value","none"))
    x= emot.emoji(spotify_list[i]).get("mean","none")
    l.append(x)   
    
pandora_file['emoji']=l

# punctuation removal

pandora_file['Rev'] = pandora_file['Rev'].str.replace('[^\w\s]','')
pandora_file['Rev'].tail()

# stop words removal

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop = set(stopwords.words('english'))
pandora_file['Rev'] = pandora_file['Rev'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
pandora_file['Rev'].head()

# number removal

pandora_file['Rev'] = pandora_file['Rev'].str.replace('\d+', '')
pandora_file['Rev'].head()


# Lemmatization

import nltk
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

lemmatizer = WordNetLemmatizer()

pandora_file['Rev']= pandora_file['Rev'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word,'n')for word in x.split()]))
pandora_file['Rev']= pandora_file['Rev'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word,'v')for word in x.split()]))
print(pandora_file['Rev'])

# spelling correction
#from autocorrect import spell 
# pandora_file['Rev']= pandora_file['Rev'].apply(lambda x: " ".join([spell(i) for i in x.split()]))

#replace words (depends on how word changes)

#pandora_file.Rev = pandora_file.Rev.str.replace('app', 'application')
#pandora_file.Rev = pandora_file.Rev.str.replace('specify', 'spotify')



# polarity
from textblob import TextBlob
pandora_file['sentiment'] = pandora_file['Rev'].apply(lambda x: TextBlob(x).sentiment[0] )
pandora_file[['Rev','sentiment']].head()

# pillars

selected_words= ['cost','cheap','expensive','reasonable','price','free','amount','charge','payment','worth','rate','costly']
selected_words=['collection','genre','selections','collections','selection','music','playlist','playlists','list','compilation','assembly','batch','cluster','combination','quantity','stock','pile','stack']
selected_words=['many', 'ads', 'adds', 'bar', 'annoying', 'pop', 'ad', 'email', 'notification', 'notifications',' emails', 'push', 'spam', 'spams']
selected_words= ['stop', 'keeps', 'stop', 'close', 'crashes', 'crash', 'start', 'load', 'closes', 'stable', 'stability']
data_frame = amazon_file['review']
#Call the function defined below
countWords(pandora_file['Rev'], selected_words)
#Import packages from libraries
import re
import string
#Define a function countWords where data frame and dictionary is passed as arguments
def countWords(data_frame, selected_words):
    words_dict = {}

    for sentence in data_frame:
        remove = string.punctuation
        remove = remove.replace("'", "") # don't remove hyphens
        pattern = r"[{}]".format(remove) # create the pattern

        test = re.sub(pattern, "", str(sentence)) #compile

        splited_words = str(test).split(' ')

        for word in splited_words:
            word = word.strip()
            word = word.lower()
            if word in selected_words:
                if word not in words_dict:
                    words_dict[word] = 1
                else:
                    words_dict[word] += 1
    return words_dict

#Count the top 20 frequently occuring words
freq = pd.Series(' '.join(pandora_file['Rev']).split()).value_counts()[:20]
print(freq)

pandora_file= pd.read_csv('C:\\Users\\gupta\\.spyder-py3\\testdata.csv')

selected_words= ['cost','cheap','expensive','reasonable','price','free','amount','charge','payment','worth','rate','costly']
selected_words=['collection','genre','selections','collections','selection','music','playlist','playlists','list','compilation','assembly','batch','cluster','combination','quantity','stock','pile','stack']
selected_words=['many', 'ads', 'adds', 'bar', 'annoying', 'pop', 'ad', 'email', 'notification', 'notifications',' emails', 'push', 'spam', 'spams']
selected_words= ['stop', 'keeps', 'stop', 'close', 'crashes', 'crash', 'start', 'load', 'closes', 'stable', 'stability']


list1 = pandora_file['Rev']
count= 0
#print(len(list1))
for j in list1:
    for k in j.split():
        if k in selected_words:
            print(j)
            count = count + 1
            break            
print(count)
                
                

    

            
    
    