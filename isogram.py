def is_isogram(word = " "):
    import string
    alpha = string.ascii_lowercase
    word = ("").join(word.split(" "))
    word = str.lower(word)
    if word == "":
        return True
    else:
        for letter in word :
            if letter not in alpha:
                continue
            elif word.count(letter) == 1:
                continue
            else :
                return False 
        return True