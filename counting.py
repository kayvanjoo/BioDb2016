def count(seq):
    count=0
    i=0
    while i+1 < len(seq):
        if seq[i] == 'G':
            if seq[i+1] == 'C':
                count=count+1
                i=i+1
        else:
            i=i+1
    return count
seq1 = "CGCGCGCgdgs"
count(seq1)  