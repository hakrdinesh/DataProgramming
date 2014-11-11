#!/usr/bin/env python
# word counter

from __future__ import print_function

import os
import sys
import string

debug = False

# application properties
testing 	= True
outdir 		= "output"
single		= False
hadoop 		= True
hadooplimit	= 0
printwords 	= False
pagermode 	= False
stopCommonWords = True
minimum_frequency = 1
minwordlen 	= 3

if (testing):
	indir = "Books"
else:
	indir = "../../../DataSetForLIFE"

def GetPathNames(indir, suffix):
	pathnames = []
	for (dir, subdirs, files) in os.walk(indir):
		if (debug):
			print("Root Directory", indir, file=sys.stderr)
			print("Subdirectories", subdirs, file=sys.stderr)
			print("Files         ", files, file=sys.stderr)
		for d in subdirs:
			if (debug):
				print("Subdirectory  ", d, file=sys.stderr)
		for f in files:
			if f.lower().endswith(suffix):
				if (debug):
					print(suffix, "File     + ", f, file=sys.stderr)
				pathname = dir + "/" + f
				if (debug):
					print(suffix, "Path     + ", pathname, file=sys.stderr)
				pathnames.append(pathname)
	if (debug):
		print("DEBUG:", suffix, "Pathnames", pathnames, file=sys.stderr)
	return pathnames

if (testing):
	outpath = indir
else:
	outpath = indir + "/" + outdir

array = GetPathNames(outpath, ".txt")



def GetOutputFileName(inputfilename, suffix = ".out"):
	outfilename = filename.replace(".txt", suffix)
	if (debug):
		print("Input File  is", filename)
		print("Output File is", outfilename)
	return outfilename

def GetInputStream(filename):
	i = open(filename, "r")
	return i

def GetOutputStream(filename):
	o = open(filename, "w")
	return o


def RemoveTrailingApostropheS(word):
	debug = False
	w = word
	while (w.endswith("'s")):
		# print("word ", word, "ends with 's")
		w = w[:-2]
		if (debug):
			print ("DEBUG RemoveTrailingApostropheS", word, w)

	return w

# End of RemoveTrailingApostropheS(word):
	
def RemoveTrailingPunctuation(word):
	debug = False
	w = word
	while (w.endswith(']') or w.endswith(')') or w.endswith('"') 
		or w.endswith('.') or w.endswith(':') or w.endswith('?') 
		or w.endswith(',') or w.endswith('/') or w.endswith('-') 
		or w.endswith("'") or w.endswith(';') or w.endswith('!') 
		or w.endswith("\\")):
		# print('word ends with ] or ) or " or . or : 
		# or ? or , or / or - or ' or ; or ! or \ 
		w = w[:-1]
		if (debug):
			print ("DEBUG RemoveTrailingPunctuation", word, w)
	# TODO: remove trailing you'd, you'll, you're
	# ( you\'d , 1 )
	# ( you\'ll , 3 )
	# ( you\'re , 1 )
	return w

# end of RemoveTrailingPunctuation()

def RemoveLeadingPunctuation(word):
	debug = False
	w = word
	while (w.startswith('[') or w.startswith('(') or 
		w.startswith('"') or w.startswith('/') or
		w.startswith(',') or w.startswith('-') or
		w.startswith("'") or w.startswith("\\")):
		# word begins with [ ( " / , - ' \
		w = w[1:]
		if (debug):
			print ("DEBUG RemoveLeadingPunctuation", word, w)
	return w

# End of RemoveLeadingPunctuation

def WordIsInsignificant(w):
	debug = False
	# skip single character words
	if (w == "?" or w == "." or w == "-"):
		if (debug):
			print("DEBUG: WordIsInsignificant", w, "True", file=sys.stderr)
		return True
	# skip empty word i.e. string of zero length
	if (w == ""):
		if (debug):
			print("DEBUG: WordIsEmpty", w, "True", file=sys.stderr)
		return True
	return False

# End of WordIsInsignificant

def PrintAllWordsAndTheirCounts(dict):
	debug = False
	# print word, frequency answers
	for key in dict:
		value = dict[key]
		if (debug):
			print ("(", key, ",", value, ")")

# End Of PrintAllWordsAndTheirCounts

def GenerateUniqueFrequencyList(words):
	# find the list of unique frequencies of words
	frequency_list_with_duplicates = sorted(words.values(), reverse=True)
	unique_frequency_set = set(frequency_list_with_duplicates)
	unique_frequency_list = list(unique_frequency_set)

	return unique_frequency_list
# End of GenerateUniqueFrequencyList

stopwords = {}

def GenerateStopWordsDictionary():
	# common words in english that typically do not add value to the meaning
	# of a document but are needed grammatically
	# ignore these words
	# note: we can have duplicates in this list
	# this is to make it easier for me
	# to add words without checking if they were present already


	stopstring = "" # note: pl keep leading space always for split() to work
	stopstring += 	" the of is to and in we"
	stopstring += 	" that a are this by that was she he "
	stopstring += 	" which her him was she he"
	stopstring += 	" his has these they be it not"
	stopstring += 	" have there no his hers an or and you but for not"
	stopstring += 	" can who when"
	stopstring += 	" from after also"
	stopstring += 	" as on if"
	stopstring += 	" our at how"
	stopstring += 	" so their other because"
	stopstring += 	" with very what then"
	stopstring += 	" your therefore cannot should"
	stopstring += 	" will many only"
	stopstring += 	" were i my them had me"
	stopstring += 	" text synonyms translation purport"
	stopstring += 	" one all may"

	# convert them to all lower case
	# trim leading and trailing whitespace
	# split them into separate words in a list called stoplist
	stoplist = stopstring.lower().strip().split()

	# store the list in a dictionary for faster access
	# you can index on a string in a dictionary
	global stopwords
	stopwords = {}
	if (stopCommonWords):
		for sw in stoplist:
			stopwords[sw] = 1

# End of GenerateStopWordsDictionary

def WordIsStopWord(w):
	global stopwords
	return w in stopwords

def WordStartsWithDigit(w):
	return (len(w) > 0) and (w[0].isdigit())

def WordStartsWithPunctuation(w):
	return (len(w) > 0) and (w[0] in string.punctuation)

def WordsIsLongEnough(w):
	if (minwordlen <= 0):
		# this check has been disabled by user, so return true always
		return True
	# assert: minwordlen > 0
	return (len(w) >= minwordlen)

def PrintImportantWordsByDecreasingFrequency(fname, ufl, words, swdict):
	oname 	= GetOutputFileName(fname, ".out.frequency")
	print("Generating output file ...", oname, file=sys.stderr)
	ofile 	= GetOutputStream(oname)
	# print frequencies of words in reducing frequency order
	print("In file ", fname, " the important words ( length >=", minwordlen, ") (by frequency) are:", file=ofile)

	global important_words
	important_words = {}

	for f in sorted(ufl, reverse=True):
		if f >= minimum_frequency:
			# print (f)
			for w in sorted(words):
				if (not (w in swdict)) and len(w) >= minwordlen:
					if words[w] == f:
						s = "( " + w + " , " + str(f) + " )"
						print(s, file=ofile)
						important_words[w] = f

# End of PrintImportantWordsByDecreasingFrequency

def PrintImportantWordsByAlphabeticOrder(fname, dict):
	oname 	= GetOutputFileName(filename, ".out.alphabetic")
	print("Generating output file ...", oname, file=sys.stderr)
	ofile 	= GetOutputStream(oname)
	print("In file ", fname, " the important words (length >=", minwordlen, ") (alphabetically) are:", file=ofile)

	# iw means important word
	for iw in sorted(dict):
		print ("(", iw, ",", dict[iw], ")", file=ofile)

# End of PrintImportantWordsByAlphabeticOrder

new_words_seen = 0

def DisplayWordIfNeeded(words, w):
	global new_words_shown
	# display new words only
	if (words[w] == 1):
		if (printwords):
			print ("(", w, ",", 1, ")")
			# display page by page if requested
			if (pagermode):
				new_words_shown = new_words_shown + 1
				if (new_words_shown % 10 == 0):
					input("Press Enter to continue")

# End of DisplayWordsIfNeeded


def TrimWord(word):
	# lower case the word
	w = word.lower()

	# remove trailing punctuation
	w = RemoveTrailingPunctuation(w)

	# remove trailing 's
	w = RemoveTrailingApostropheS(w)

	# remove leading punctuation
	w = RemoveLeadingPunctuation(w)
	return w

# end of TrimWord

def WordCount(filename):
	iname 	= filename
	f 	= GetInputStream(iname)

	# dictionary of words
	words = {}
	new_words_shown = 0
	nhadoop = 0

	for line in f:
		# print (line)
		for word in line.strip().split():

			w = TrimWord(word)

			if "(" in w:
				wlist = w.split('(')
				w = wlist.pop()
				w = TrimWord(w)

			if "[" in w:
				wlist = w.split('[')
				w = wlist.pop()
				w = TrimWord(w)
			
			# skip single character words or empty words
			if WordIsInsignificant(w):
				# skip it, continue on to the next word
				continue
			
			# skip single character words or empty words
			if WordIsInsignificant(w):
				# skip it, continue on to the next word
				continue

			# skip very short words i.e. len < minwordlen
			if not WordsIsLongEnough(w):
				# skip it, continue on to the next word
				continue

			# skip words starting with numbers
			if WordStartsWithDigit(w):
				# skip it, continue on to the next word
				continue

			# skip words starting with punctuation
			if WordStartsWithPunctuation(w):
				# skip it, continue on to the next word
				continue

			# skip stop words
			if stopCommonWords and WordIsStopWord(w):
				# skip it, continue on to the next word
				continue

			# for hadoop, just print that we have seen this word
			if (hadoop):
				if (hadooplimit > 0):
					nhadoop += 1
				print ( "{0}\t{1}".format(w, 1) )
				if (hadooplimit > 0):
					if (nhadoop == hadooplimit):
						return
				continue;

			# assert: not in hadoop mode
			# let us count the occurrences of all words 
			# check if we have seen this word
			if not (w in words):
				# we have seen now 1 occurrence of this word
				words[w] = 1
			else:
				# we have seen 1 more occurrence of this word
				frequency = words[w]
				words[w] = frequency + 1

			DisplayWordIfNeeded(words, w)

		# end of for word in line.strip().split():
	# end of for line in f:

	# no further processing for hadoop style program
	if (hadoop):
		return

	# print all words and their frequencies (we call it counts)
	PrintAllWordsAndTheirCounts(words)

	# generate a list of common words and put them into a dictionary

	# compiles of list of unique frequencies
	# if we see frequencies like: 34, 34, 300, 1, 1, 1
	# we want to remember that there was 300 then 34 then 1
	# so we need a list of unique frequencies in descending order
	unique_frequency_list = GenerateUniqueFrequencyList(words)

	# print all words with their counts
	# most frequent word first
	# least frequent word last
	PrintImportantWordsByDecreasingFrequency(filename, 
				unique_frequency_list, words, stopwords)

	# print all words in alphabetic order and their counts
	PrintImportantWordsByAlphabeticOrder(filename, important_words)

# end of WordCount

GenerateStopWordsDictionary()
for f in array:
	filename = f
	# process only 1 file i.e. singlemode
	if (single):
		# skip if not ssr.txt, favourite book to read
		if not (filename == "Books/ssr.txt"):
			if debug:
				print("Skipping file", filename, file=sys.stderr)
			continue
		# process only ssr.txt
	print("Processing", filename, file=sys.stderr)
	WordCount(filename)

exit(0)
