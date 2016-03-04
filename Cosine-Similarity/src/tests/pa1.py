'''
Created on Feb 14, 2015

@author: Puneeth U Bharadwaj
'''

import os, math
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import OrderedDict

corpus_root = 'F:/Studies/Second Sem - Spring 2015/CSE5334 - Data Mining/PA 1 - NLTK/stateoftheunionaddresses'

stopwords = stopwords.words('english')

corpus = {}

speeches = {}

count = 0

president = []

def pub_frequency(term, terms):
    return terms.count(term)

def pub_tf(term, terms):
    frequency_of_term = pub_frequency(term, terms)
    length_of_term = len(terms)
    return (frequency_of_term/float(length_of_term))

def num_docs_containing(tf, president):
    count = 0
    for pres in president:
#         if (pub_frequency(tf, pres)) > 0:
#             count = count + 1
        if tf in pres:
            count = count + 1
    
    return 1 + count

def pub_idf(tf, president):
    return math.log10(len(president)/float(num_docs_containing(tf, president)))

def pub_tf_idf(term, terms, president):
    tef = pub_tf(term, terms)
    idef = pub_idf(term, president)
    return(tef * idef)

def docdocsim(filename1, filename2):
    vec1 = speeches[filename1]['tf-idf']
    vec2 = speeches[filename2]['tf-idf']
    
    intersection = set(vec1.keys()) & set(vec2.keys())     
    print(intersection)
    
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    print(numerator)
     
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
     
    if not denominator:
        return 0.0
    else:
        cosine = float(numerator) / denominator
        print(str(cosine))

print('Reading files into a dictionary')
for filename in os.listdir(corpus_root):
    file = open(os.path.join(corpus_root, filename), 'r')
    filetext = file.read()
    corpus[filename] = str(filetext)

tokenizer = RegexpTokenizer(r'[a-zA-Z]+')

corpus2 = OrderedDict(sorted(corpus.items(), key=lambda t: t[0]))
# for i in corpus2:
#     print(i)

print('Tokenizing, finding frequency of each term and find Term Frquency')
for filename in corpus2:
    print(filename)
    
    filetext = corpus[filename]
    terms = tokenizer.tokenize(filetext)
    terms = [term.lower() for term in terms]
    terms = [term for term in terms if term not in stopwords]
    stemmer = PorterStemmer()
    terms = [stemmer.stem(term) for term in terms]

    terms.sort()        
    
    speeches[filename] = {'frequency':{}, 'tf':{}, 'idf':{}, 'tf-idf':{}, 'terms':{}}
    
    for term in terms:
        #Frequency of each term in the each speech
        speeches[filename]['frequency'][term] = pub_frequency(term, terms)
        #Term Frequency for each term in the each speech
        speeches[filename]['tf'][term] = speeches[filename]['frequency'][term]/float(len(terms))
        speeches[filename]['terms'] = terms
    
    t = list(set(terms))
    t.sort()
    president.append(t)
     
#     count = count + 1
#     if count == 2:
#         break

# print(president)

print('Finding Inverse Document Frequency and TF-IDF')
for speech in speeches:
    for tf in speeches[speech]['tf']:
        print(tf)
        #Inverse Document Frequency 
        speeches[speech]['idf'][tf]= pub_idf(tf, president)
        #The tf-idf
#         speeches[speech]['tf-idf'][tf]= pub_tf_idf(tf, speeches[speech]['terms'], president)
        speeches[speech]['tf-idf'][tf] = speeches[filename]['tf'][term] * speeches[speech]['idf'][tf]
        
for speech in speeches:
    print(speech, speeches[speech]['tf-idf'])

print('Finding Cosine Similarity between two documents')
# docdocsim('Barack ObamaJanuary 20, 2015.txt', 'Barack ObamaJanuary 28, 2014.txt')