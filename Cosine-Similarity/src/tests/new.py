'''
Created on Feb 14, 2015

@author: Puneeth U Bharadwaj
'''

import os, math
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import OrderedDict, Counter

corpus_root = 'F:/Studies/Second Sem - Spring 2015/CSE5334 - Data Mining/PA 1 - NLTK/stateoftheunionaddresses'

stopwords = stopwords.words('english')

corpus = {}

speeches = {}

count = 0

president = []
print('Reading files into a dictionary')
for filename in os.listdir(corpus_root):
    file = open(os.path.join(corpus_root, filename), 'r')
    filetext = file.read()
    corpus[filename] = str(filetext)
    
    count =  count + 1
    
#     if count == 30:
#         break
    
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')

corpus2 = OrderedDict(sorted(corpus.items(), key=lambda t: t[0]))

print('Tokenizing and finding Term Ferquency')
for filename in corpus2:
#     print(filename)
    filetext = corpus2[filename]
    
    filetext = corpus[filename]
    terms = tokenizer.tokenize(filetext)
    terms = [term for term in terms if term not in stopwords]
    terms = [term.lower() for term in terms]
    stemmer = PorterStemmer()
    terms = [stemmer.stem(term) for term in terms]

    terms.sort()     
    
    speeches[filename] = {'tf':{}, 'idf':{}, 'tf-idf':{}, 'terms':{}}
    
    l = float(len(terms))
    
    speeches[filename]['tf'] = Counter(terms)
    speeches[filename]['terms'] = terms
    
#     for term in terms:
#         #Term Frequency for each term in the each speech
#         speeches[filename]['tf'][term] = terms.count(term)
#         speeches[filename]['terms'] = terms
    
    t = list(set(terms))
    t.sort()
    president.append(t)

l = len(president)

sorted_speeches = OrderedDict(sorted(corpus.items(), key=lambda t: t[0]))

print('Finding Inverse Document Frequency and TF-IDF')
for speech in sorted_speeches:
    print(speech)
    for word in speeches[speech]['tf']:
        count = 0
        
        for pres in president:
            if word in pres:
                count =  count + 1
        
        try:
            speeches[speech]['idf'][word]= math.log(l/float(count))
            if speeches[filename]['tf'][word] == 0:
                speeches[speech]['tf-idf'][word] = 0
            if speeches[filename]['tf'][word] > 0:
                speeches[speech]['tf-idf'][word] = (1 + math.log(abs(speeches[filename]['tf'][word]))) * speeches[speech]['idf'][word]
                
        except KeyError:
            print(speech, ',', word)
        except ValueError:
            print(speech, ',', word, ',', speeches[filename]['tf'][word])
        
print(speeches['Barack ObamaJanuary 20, 2015.txt']['tf-idf'])