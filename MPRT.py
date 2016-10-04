
# coding: utf-8

# In[1]:

import re
import requests
from Bio import SeqIO
from io import StringIO


motif = re.compile('(?=N[^P][ST][^P])')

fid = open('rosalind_mprt.txt','r')
accs = fid.read().strip().split('\n')
fid.close()


for acc in accs:
    r = requests.get('http://www.uniprot.org/uniprot/%s.fasta' % acc)
    raw_data = SeqIO.read(StringIO(r.text), 'fasta')
    locations = []
    
    # Use search instead of match to search entire string
    if re.search(motif, str(raw_data.seq)):
        print(acc.strip())
        for m in re.finditer(motif, str(raw_data.seq)):
            locations.append(m.start()+1)
        print(" ".join(map(str, locations)))

