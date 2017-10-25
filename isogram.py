def is_isogram(word = " "):
    x = 0
    word_2 = str.upper(word)
    for letter in word_2 :
        if word_2.count(letter) == 1 and letter != " " :
            x = x+1
            if len(word_2) == x :
                print(word + " is an isogram.")
                return True
        elif letter == " " :
            x = x
            if len(word_2) == x :
                return True
            else :
                continue
        else :
            print(word + " is not an isogram.")
            return False


# Interpretes spaces as letters, hence doesn't know what to do with them   