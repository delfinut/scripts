#!/usr/bin/env python

#######

# Description: 
# Script to replace current fasta headers with new headers by looking up and matching from a tab delimited file 
# called "newnames.txt" which has current headers in the first column and new headers in the second column 
# outputs a fasta file with new headers whose name has "-newIDs.fa" appended to the original input file name.


# Usage:
# newIDs.py [fastafile in which headers need to be replaced]


# TO DO to improve script

# argparse to be able to input fasta file and names file with -f and -n arguments 
# (I get confused which goes first when using just sys.argv so the name of the tab delimited file is fixed for the moment)

# test script formally

# make it a function that can be used as part of other scripts

#######

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
            #print("Old ID is", record.id) #Testing
            record.id = pairdict.get(record.id)
            #print("New ID is", record.id) #Testing
            record.description = record.id 
            # above makes it not provide old and new names in header, just new
        SeqIO.write(record, corrected, 'fasta')

print("fini!")
