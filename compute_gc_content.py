#!/usr/bin/python
"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset

>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output

Rosalind_0808
60.919540
"""

from __future__ import division
from __future__ import print_function
import sys
import re

def getGcContent(seq):
	length = len(seq)
	gCount = seq.count('G')
	cCount = seq.count('C')
	gcContent = round((gCount + cCount)/length, 6) * 100
	return str(gcContent) 

filename = sys.argv[1]
fastaFile = open(filename)

started = 0
nucleotideSeq = ""

for line in fastaFile:
	line = line.rstrip('\n') # remove newline from each line

	# if the line does not contain an alphanumeric character, skip it and go to the next line:
	if not(re.search('[a-zA-Z0-9]', line)):
		continue

	# if it's the defline:
	if line.startswith('>'):
		# if this is not the first sequence record in the fasta file
		# print the GC content of the last record:
		if started == 1:
			print(getGcContent(nucleotideSeq))

		# now print the sequence ID in the current defline:
		line = line.replace('>', '', 1) # replace only the first occurrence of '>'
		lineArray = line.split()
		print(lineArray[0], end ="\n")

		# remove contents of nucleotideSeq variable:
		nucleotideSeq = ""

	else:
		line = line.upper()
		nucleotideSeq += line

	started = 1

# print GC content of last nucleotide sequence entry:
print(getGcContent(nucleotideSeq))

fastaFile.close()
