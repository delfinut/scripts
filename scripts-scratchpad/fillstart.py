#!/anaconda/bin/python3.5

import sys 
import os
from Bio import SeqIO
from Bio import AlignIO

infile="test.fa"

outfile=os.path.splitext(infile)[0]+"-fillstart.fa"


with open(infile) as original, open(outfile, 'w') as corrected:
    alignment = AlignIO.read(original, "fasta")
    print("Alignment length is %i" % alignment.get_alignment_length())
    #records = AlignIO.parse(infile, 'fasta')
    #print(records.id)
    #for record in records:         
    #    if record.id in pairdict:
    #        #print("Old ID is", record.id)
    #        record.id = pairdict.get(record.id)
    #        #print("New ID is", record.id)
    #        record.description = record.id # <- Add this line
    #   SeqIO.write(record, corrected, 'fasta')

print("fini!")