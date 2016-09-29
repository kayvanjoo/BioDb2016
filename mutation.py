def mutation(seq1,seq2):
    count=0
    i=0
    mn=min(len(seq1),len(seq2))
    while i+1 < mn:
        if seq1[i] != seq2[i]:
            count=count+1
            i=i+1
        else:
            i=i+1
    return count
seq1 = "CGCGCGCgdgs"
seq2 = "fffffffgs"
mutation(seq1,seq2)