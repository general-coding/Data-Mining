'''
Created on Feb 10, 2015

@author: Puneeth U Bharadwaj
'''

import re, math
from collections import Counter
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# WORD = re.compile(r'[a-zA-Z]+')
tokenizer = RegexpTokenizer(r'[a-zA-Z\']+')
stopwords = stopwords.words('english')

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    print(intersection)
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
#     words = WORD.findall(text)    
    words = tokenizer.tokenize(text)
    print(type(words))
    return Counter(words)

def querydocsim(qstring,filename):
    vector1 = text_to_vector(qstring)
    
    with open(filename, mode='r') as f:
        filetext  = str(f.read()).lower()
    
    vector2 = text_to_vector(filetext)
    
    vector3 = Counter()
    
    for key in vector2:
        if key not in stopwords:
            vector3[key] = vector2[key]
    
    cosine = get_cosine(vector1, vector3)
    print('querydocsim - cosine similarity - ', cosine)
    
def docdocsim(filename1,filename2):
    with open(filename1, mode='r') as f:
        filetext  = str(f.read()).lower()
    
    vectorx = text_to_vector(filetext)    
    vector1 = Counter()
    
    for key in vectorx:
        if key not in stopwords:
            vector1[key] = vectorx[key]
            
    filetext = ' '
            
    with open(filename2, mode='r') as f:
        filetext  = str(f.read()).lower()
    
    vectory = text_to_vector(filetext)    
    vector2 = Counter()
    
    for key in vectory:
        if key not in stopwords:
            vector2[key] = vectory[key]
    
    cosine = get_cosine(vector1, vector2)
    print('docdocsim - cosine similarity - ', cosine)
    
# querydocsim('health insurance wall street', '../stateoftheunionaddresses/Barack ObamaJanuary 28, 2014.txt')
querydocsim('health insurance wall street', '../stateoftheunionaddresses/Barack ObamaJanuary 28, 2014.txt')
docdocsim('../stateoftheunionaddresses/Barack ObamaJanuary 20, 2015.txt', '../stateoftheunionaddresses/Barack ObamaJanuary 28, 2014.txt')