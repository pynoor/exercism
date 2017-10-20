def isogram(word = " "):
    x = 0
    for letter in word :
        if word.count(str(letter)) == 1:
            x = x+1
            if len(word) == x :
                print (word + "is an isogram.")
            
        else :
            print(word + " is not an isogram.")
            break
 
