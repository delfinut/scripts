#!/usr/bin/env python

import sys 
import os
from Bio import SeqIO

infile=sys.argv[1]
names="newnames.txt"
outfile=os.path.splitext(infile)[0]+"-newIDs.fa"


namesdata = []
with open(names, "r") as fh1: #open to read "r"
    for line in fh1:
        namesdata.append(line.strip())

pairdict = {}
for line in namesdata:
    chunks = line.split("\t")
    if chunks != ['']:
        oldname = chunks[0]
        newname = chunks[1]
        pairdict[oldname] = newname

with open(infile) as original, open(outfile, 'w') as corrected:
    records = SeqIO.parse(infile, 'fasta')
    for record in records:         
        if record.id in pairdict:
            #print("Old ID is", record.id)
            record.id = pairdict.get(record.id)
            #print("New ID is", record.id)
            record.description = record.id 
            # makes it not provide old and new names in header, just new
        SeqIO.write(record, corrected, 'fasta')

print("fini!")