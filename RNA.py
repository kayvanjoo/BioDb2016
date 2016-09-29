def DNA2RNA(sequence):
    for x in sequence:
        sequence=sequence.replace('T','U')
    return sequence

l="AAATTTGGGGGGG"
DNA2RNA(l)