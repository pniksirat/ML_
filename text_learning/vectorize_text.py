#!/usr/bin/python

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

import os
import pickle
import re
import sys
import numpy as np

sys.path.append( "C:\\Users\\pniksirat\\Downloads\\ud120-projects-master\\ud120-projects-master\\tools" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""
dir=os.path.join(os.path.abspath(os.curdir),"text_learning")
os.chdir(dir)
from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")
os.chdir("..")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
       # if temp_counter < 200:
        path = os.path.join('..', path[:-1])
        print(path)
        email = open(path, "r")

        ### use parseOutText to extract the text from the opened email
        text = parseOutText(email)
        ### use str.replace() to remove any instances of the words
        ### ["sara", "shackleton", "chris", "germani"]
        sig=["sara", "shackleton", "chris", "germani"]
        text_mod=text
        for key in sig:  
            text_mod = text_mod.replace( key, "" )
        ### append the text to word_data
        word_data.append(text_mod)
        ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
        if name=="sara":
            from_data.append(0)
        else :
            from_data.append(1)

        email.close()

print("emails processed")
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "wb") )
pickle.dump( from_data, open("your_email_authors.pkl", "wb") )





### in Part 4, do TfIdf vectorization here

#removing stop words
filtered_sentence=[]
filtered_temp=[]
filtered=[]
stop_words = set(stopwords.words('english')) 
word_tokens = [word_tokenize(x) for x in word_data]  
for i in range(len(word_data)):
    filtered_sentence.append([w for w in word_tokens[i] if not w in stop_words])
for i in range(len(word_data)): 
    for w in word_tokens[i]: 
     if w not in stop_words: 
        filtered_temp.append(w)
    filtered.append(np.array(filtered_temp))
    filtered_temp=[]

filtered_Str=[]
for i in range(len(filtered)):
    filtered_Str.append((''.join(filtered[i])))

pipe = Pipeline([('vect', CountVectorizer()),('tfid', TfidfTransformer())]).fit(filtered_Str)
pipe['vect'].transform(filtered_Str).toarray()

pipe['tfid'].idf_

pipe.transform(filtered_Str).shape 

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(filtered_Str)
print(vectorizer.get_feature_names())

print(X.shape)
