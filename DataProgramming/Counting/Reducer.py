#!/C/Python34/python.exe

import sys

debug = False

f = sys.stdin
ow = None
sum = 0
for line in f:
	l = line.strip()
	if l == "":
		continue
	if (debug):
		print("DEBUG: Line is", l, file=sys.stderr)
	try:
		(nw, nc) = l.split("\t")
		if (debug):
			print( nw, "=", nc, flush=True )
		nf = int(nc)
		if not nw == ow:
			first = (ow == None)
			# new word seen, so print old word and count
			# also, for the first time, no need to print old word
			# as it is None
			if not first:
				print ( "(", ow, ",", sum, ")", flush=True )
			# update the old word and sum to latest
			ow = nw
			sum = nf
		else:
			# word has been repeated so please update sum
			sum += nf
	except:
		continue

print ( "(", ow, ",", sum, ")", flush=True )
