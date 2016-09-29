from Bio import ExPASy
from Bio import SwissProt

with open('rosalind_dbpr.txt') as input_data:
	UniProt_ID = input_data.read().strip()

handle = ExPASy.get_sprot_raw(UniProt_ID)
record = SwissProt.read(handle)

bio_proc = []
for item in record.cross_references:
    if item[0] == 'GO' and item[2][0]=='P':
        bio_proc.append(item[2].lstrip('P:'))

print ('\n'.join(bio_proc))
with open('Armory_002_DBPR.txt', 'w') as output_data:
    output_data.write('\n'.join(bio_proc))