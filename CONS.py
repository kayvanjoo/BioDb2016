
# coding: utf-8

# In[1]:

from Bio import motifs
from Bio.Seq import Seq
import Bio.Alphabet

f = open("rosalind_cons.txt", 'r')
raw_data = f.readlines()
f.close()

motif_dict = {}
cur_key = ''

#create dic with id as key and seq as value
for i in raw_data:
    if i[0] == '>':
        cur_key = i[1:].rstrip()
        motif_dict[cur_key] = '' 
    else:
        motif_dict[cur_key] += i.rstrip()

# create motifs instances
instances = []
for seq in motif_dict.values():
    instances.append(Seq(seq))
m = motifs.create(instances)


profile = m.counts # creates a profile matrix
consensus = m.consensus

print (consensus)
for key, value in profile.items():
    # must convert integers to str for concatenating
    print ( "".join(key + ": " + " ".join(map(str, value))))

