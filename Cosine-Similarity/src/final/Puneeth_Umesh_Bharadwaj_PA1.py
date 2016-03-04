'''
Created on Feb 14, 2015

@author: Puneeth U Bharadwaj

References -
https://docs.python.org/2/library/stdtypes.html#set
https://docs.python.org/2/library/stdtypes.html?highlight=dictionary#dict
https://docs.python.org/2/library/collections.html?highlight=counter#collections.Counter
https://docs.python.org/2/library/stdtypes.html?highlight=dictionary#set-types-set-frozenset
https://docs.python.org/2/library/stdtypes.html?highlight=dictionary#dictionary-view-objects
https://docs.python.org/2/tutorial/datastructures.html?highlight=dictionary#list-comprehensions
'''

import os, math, time
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter

start = time.time()

corpus_root = 'stateoftheunionaddresses'
stopwords = stopwords.words('english')
stopwords.sort()
corpus = {}
tf_dict = {}
idf_dict = {}
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
stemmer = PorterStemmer()

print('Reading files into a dictionary \n')
for filename in os.listdir(corpus_root):
    file = open(os.path.join(corpus_root, filename), 'r')
    filetext = file.read()
    corpus[filename] = str(filetext)
    
print('Tokenizing, Stemming and TF \n')
for filename in corpus:
    filetext = corpus[filename]
    
    terms = tokenizer.tokenize(filetext)
    terms = [term.lower() for term in terms]
    terms = [term for term in terms if term not in stopwords] 
    terms = [stemmer.stem(term) for term in terms]

    tf_dict[filename] = {}    
    tf_dict[filename] = Counter(terms)
    
temp = tf_dict

a = ' '
print('Finding IDF of each word \n')
for filename in tf_dict:
    for word in tf_dict[filename]:
        count = 0
        try:
            for file in temp:
                if word in temp[file]:
                    count = count + 1            
        except KeyError:
            a = a + word
        
        idf_dict[word] = math.log10(len(tf_dict) / float(count))

def getqvec(qstring):  
    qterms = tokenizer.tokenize(qstring)
    qterms = [qterm.lower() for qterm in qterms]
    qterms = [qterm for qterm in qterms if qterm not in stopwords]
    qterms = [stemmer.stem(qterm) for qterm in qterms]
    
    tf_qterms = {}
    tf_qterms = Counter(qterms)
    
    tf_wt = {}    
    for term in tf_qterms:
        tf_wt[term] = 1 + math.log10(tf_qterms[term])
        
    tf_idf_wt= {}
    for term in tf_wt:
        tf_idf_wt[term] = tf_wt[term] * idf_dict[term]
        
    d = 0
    for term in tf_idf_wt:
        d = d + math.pow(tf_idf_wt[term], 2)
    
    normd = math.sqrt(d)
    
    qvec = {}
    for term in tf_idf_wt:
        qvec[term] = tf_idf_wt[term]/normd        
    
    return qvec

def gettfidfvec(filename):
    tf_wt = {}
    tf_idf_file = {}
    for term in tf_dict[filename]:
        tf_term = tf_dict[filename][term]
        tf_wt[term] = 1 + math.log10(tf_term)
        tf_idf_file[term] = tf_wt[term] * idf_dict[term]
        
    d = 0
    for term in tf_idf_file:
        d = d + pow(tf_idf_file[term], 2)
    
    normd = math.sqrt(d)
        
    tfidfvec = {}
    for term in tf_idf_file:
        tfidfvec[term] = tf_idf_file[term]/normd 
          
    return tfidfvec
    
def getidf(query):
    return idf_dict[query]

def docdocsim(filename1, filename2):
    cosine = 0
    tfidf_f1 = gettfidfvec(filename1)
    tfidf_f2 = gettfidfvec(filename2)
    
    common = set(tfidf_f1) & set(tfidf_f2)
    
    a = ' '
    for word in common:
        try:
            cosine = cosine + (tfidf_f1[word] * tfidf_f2[word])
            
        except KeyError:
            a = a + ' '
            
    print(cosine)

def querydocsim(query, filename):
    cosine = 0
    tfidf_q = getqvec(query)
    tfidf_f = gettfidfvec(filename)
    
    common = set(tfidf_q) & set(tfidf_f)
    a = 0
    
    for word in common:
        try:
            cosine = cosine + (tfidf_q[word] * tfidf_f[word])
            
        except KeyError:
            a = a + 1
    
    return cosine

def query(qstring):
    q = {}
    for filename in corpus:
        q[filename] = querydocsim(qstring, filename)
    
    sorted_speeches = sorted(q.items(), key=lambda t: t[1], reverse=True)
    
    print(sorted_speeches[0][0])

print(getqvec("health insurance wall street"))

print(query("health insurance wall street"))

print(gettfidfvec("Barack ObamaJanuary 20, 2015.txt"))

print(getidf("health"))

print(docdocsim("Barack ObamaJanuary 20, 2015.txt", "Barack ObamaJanuary 28, 2014.txt"))

print(querydocsim("health insurance wall street", "Barack ObamaJanuary 28, 2014.txt"))

end = time.time()

print(end-start)