def is_isogram(word = " "):
    x = 0
    for letter in word :
        if word.count(str(letter)) == 1:
            x = x+1
            if len(word) == x :
                return (word + " is an isogram.")
            
        else :
            print(word + " is not an isogram.")
            return False

# takes into consideration that capital and small letters are different
            