#!/C/Python27/python.exe
from __future__ import print_function

import sys

debug = False

f = sys.stdin
ow = None
sum = 0
# for all lines in file
for line in f:
	# remove leading and trailing whitespace
	l = line.strip()
	# skip if line is empty
	if l == "":
		continue
	if (debug):
		print("DEBUG: Line is", l, file=sys.stderr)
	# wrap in try except for int conversion and line split exceptions
	try:
		# split line into newly seen newword, newoccurence
		(nw, nc) = l.split("\t")
		if (debug):
			print( nw, "=", nc )
		# convert newoccurrence string to newfrequency integer
		nf = int(nc)
		# if newword is different from word
		if not nw == ow:
			# is the first word that we see?
			first = (ow == None)
			# new word seen, so print old word and count
			# also, for the first time, no need to print old word
			# as it is None
			if not first:
				print ("(", ow, ",", sum, ")")
			# then, update the old word and sum to latest
			ow = nw
			sum = nf
		else:
			# word has been repeated so please update sum
			sum += nf
	except:
		continue

print ("(", ow, ",", sum, ")")
