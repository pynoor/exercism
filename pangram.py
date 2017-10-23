def is_pangram(sentence = "This is a sentence"):
    count = 0
    new = str.lower(sentence)
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",\
                    "o","p","q","r","s","t","u","v","w","x","y","z"]
    for x in alphabet :
        if x in new :
            count = count + 1
    if count >= 26 :
        return True
    else :
        return False
            
            
