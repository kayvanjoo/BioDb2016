def complement(seq):
    i=0
    while i+1 < len(seq):
        if seq[i]=='A' :
            seq=seq.replace('A','T')
            i=i+1
        elif seq[i]=='T':
            seq=seq.replace('T','A')
            i=i+1
        elif seq[i]=='G':
            seq=seq.replace('G','C')
            i=i+1
        elif seq[i]=='C':
            seq=sequence.replace('C','G')
        else:
            i=i+1
        else:
            i=i+1
        
    return seq
               
seq1 = "AAATTTGGGGGGG"
complement(seq1)              


