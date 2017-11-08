
import re
def word_count(phrase):
    words = phrase.split()
    frequencies = []
    new = []
    for x in words :
        regex = re.compile('[^a-zA-Z]')
        regex = regex.sub('', str(x)) 
        frequencies.append(words.count(x))
        if str(regex) == "" :
            continue
        new.append("'" + str(regex) + "'" + " : " + str(frequencies[words.index(x)]))

    return (new)