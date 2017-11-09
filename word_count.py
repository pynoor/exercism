
import re
import string

def word_count(phrase):
    
    phrase = phrase.lower()
    
    def extract_words(s):
        return[re.sub('^[{0}]+|[{0}]+$'.format(string.punctuation), '', w) for w in phrase.split()]
        
    words = extract_words(phrase)
    print(words)
    frequencies = []
    new = dict()
    
    for x in words :   
        frequencies.append(words.count(x))  
        if str(x) == "" :
            continue
        new[x] = frequencies[words.index(x)]
        
    return (new)
