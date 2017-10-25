def to_rna(dna_strand):
    for letter in dna_strand :  
        if letter == "G" :
            x = ["C", dna_strand.index(letter)]
        elif letter == "C" :
            y = ["G", dna_strand.index(letter)]
        elif letter == "T" :
            z = ["A", dna_strand.index(letter)]
        elif letter == "A" :
            v = ["U", dna_strand.index(letter)]
    def takeSecond(elem) :
        return elem[1]
    total = [x, y, z, v]
    total.sort(key = takeSecond)
    output = ""
    for s in total :
        output = output + str(x[0])
    return (output)

# Does not work for input that does not consist of all the letters G, C, T, A.