
# -*- coding: utf-8 -*-


import pandas as pd 
spotify_file= pd.read_csv('C:\\Users\\gupta\\.spyder-py3\\spotify3.csv')
print(spotify_file)

# to lower case

spotify_file['Review']= spotify_file['Review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
spotify_file['Review'].head()

# exract emoji 

import emot

spotify_list =spotify_file['Review']
l=[]
for i in range(len(spotify_list)):
    #print (emot.emoji(reviewlist[i]).get("value","none"))
    x= emot.emoji(spotify_list[i]).get("mean","none")
    l.append(x)   
    
spotify_file['emoji']=l

# punctuation removal

spotify_file['Review'] = spotify_file['Review'].str.replace('[^\w\s]','')
spotify_file['Review'].tail()

# stop words removal

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop = set(stopwords.words('english'))
spotify_file['Review'] = spotify_file['Review'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
spotify_file['Review'].head()

# number removal

spotify_file['Review'] = spotify_file['Review'].str.replace('\d+', '')
spotify_file['Review'].head()


# Lemmatization

import nltk
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

lemmatizer = WordNetLemmatizer()

spotify_file['Review']= spotify_file['Review'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word,'n')for word in x.split()]))
spotify_file['Review']= spotify_file['Review'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word,'v')for word in x.split()]))
print(spotify_file['Review'])

# spelling correction
from autocorrect import spell 
spotify_file['Review']= spotify_file['Review'].apply(lambda x: " ".join([spell(i) for i in x.split()]))

#replace words (depends on how word changes)

spotify_file.Review = spotify_file.Review.str.replace('app', 'application')
spotify_file.Review = spotify_file.Review.str.replace('specify', 'spotify')




# polarity
from textblob import TextBlob
spotify_file['sentiment'] = spotify_file['Review'].apply(lambda x: TextBlob(x).sentiment[0] )
spotify_file[['Review','sentiment']].head()


# sentiment

spotify_file['sentiment'] = spotify_file['Review'].apply(lambda x: TextBlob(x).sentiment[0] )
spotify_file[['Review','sentiment']].head()


selected_words= ['cost','cheap','expensive','reasonable','price','free','amount','charge','payment','worth','rate','costly']
selected_words=['collection','genre','selections','collections','selection','music','playlist','playlists','list','compilation','assembly','batch','cluster','combination','quantity','stock','pile','stack']
selected_words=['many', 'ads', 'adds', 'bar', 'annoying', 'pop', 'ad', 'email', 'notification', 'notifications',' emails', 'push', 'spam', 'spams']
selected_words= ['stop', 'keeps', 'stop', 'close', 'crashes', 'crash', 'start', 'load', 'closes', 'stable', 'stability']
selected_words= ['music']

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
