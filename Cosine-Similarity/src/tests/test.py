'''
Created on Feb 10, 2015

@author: Puneeth U Bharadwaj
'''

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

tokenizer = RegexpTokenizer(r'[a-zA-Z\']+')
stopwords = stopwords.words('english')
stemmer = PorterStemmer()

terms = tokenizer.tokenize("puneeth's laptop is awesome. he's the best.")
terms = [stemmer.stem(term) for term in terms]
print(terms)  