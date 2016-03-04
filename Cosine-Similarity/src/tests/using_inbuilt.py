'''
Created on Feb 10, 2015

@author: Puneeth U Bharadwaj
'''

from __future__ import division
import nltk
import random
import re, pprint, os, numpy

# Code to read in a directory of text files, create nltk.Text objects out of them,
# load an nltk.TextCollection object and create a BOW with TF*IDF values.

# First set the variable path to the directory path.  Use
# forward slashes (/), even on Windows.  Make sure you
# leave a trailing / at the end of this variable.

# Path for mac OS X will look something like this:
path = 'F:/Studies/Second Sem - Spring 2015/CSE5334 - Data Mining/PA 1 - NLTK/stateoftheunionaddresses/'

# Empty list to hold text documents.
texts = []
count = 0
# Iterate through the  directory and build the collection of texts for NLTK.
listing = os.listdir(path)
for infile in listing:
    if infile.startswith('.'): #Mac directories ALWAYS have a .DS_Store file.
        continue               #This ignores it and other hidden files.
    url = path + infile
    f = open(url);
    raw = f.read()
    f.close()
    tokens = nltk.word_tokenize(raw) 
    text = nltk.Text(tokens)
    texts.append(text)
    
print ("Prepared ", len(texts), " documents...")
print ("They can be accessed using texts[0] - texts[" + str(len(texts)-1) + "]")

#Load the list of texts into a TextCollection object.
collection = nltk.TextCollection(texts)
print ("Created a collection of", len(collection), "terms.")

#get a list of unique terms
unique_terms = list(set(collection))
print ("Unique terms found: ", len(unique_terms))

# Function to create a TF*IDF vector for one document.  For each of
# our unique words, we have a feature which is the td*idf for that word
# in the current document
def TFIDF(document):
    word_tfidf = []
    for word in unique_terms:
        word_tfidf.append(collection.tf_idf(word,document))
    return word_tfidf

### And here we actually call the function and create our array of vectors.
for f in texts:
    print(f)

vectors = [numpy.array(TFIDF(f)) for f in texts]
print ("Vectors created.")
print ("First 10 words are", unique_terms[:10])
print ("First 10 stats for first document are", vectors[0][0:])