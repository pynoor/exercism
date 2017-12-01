def to_rna(dna_strand):
    RNA = {"G":"C", "C":"G", "T":"A", "A":"U"}
    dna_list = list(dna_strand)
    rna_list = []
    for x in dna_list:
        if x not in RNA:
            return ""
        rna_list.append(RNA[x])
    return "".join(rna_list)
        