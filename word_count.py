
import re
def word_count(phrase):
    
    words = phrase.split()
    frequencies = []
    new = dict()
    
    for x in words :   
        frequencies.append(words.count(x))  
        regex = re.compile('[^a-zA-Z]')
        regex = regex.sub('', str(x)) 
        if str(regex) == "" :
            continue
        new[regex] = frequencies[words.index(x)]
        
    return (new)

