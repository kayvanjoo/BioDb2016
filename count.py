def count(sequence):
    fin=open(sequence)
    print('G count is: ', sequence.count('G'))
    print('A count is: ', sequence.count('A'))
    print('C count is: ', sequence.count('C'))
    print('T count is: ', sequence.count('T'))
l="AAATTTGGGGGGG"
count(l)