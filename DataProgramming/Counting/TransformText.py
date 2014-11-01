#!/C/Python34/python.exe
# utf8 to ascii conversion
import os
import sys
import PyPDF2

debug		= True
testing 	= True


outdir = "output"
suffix = ".utf8"

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
			print("Subdirectory  ", d, file=sys.stderr)
		for f in files:
			if f.lower().endswith(suffix):
				print(suffix, "File     + ", f, file=sys.stderr)
				pathname = dir + "/" + f
				print(suffix, "Path     + ", pathname, file=sys.stderr)
				pathnames.append(pathname)
	print("DEBUG:", suffix, "Pathnames", pathnames)
	return pathnames

if (testing):
	outpath = indir
else:
	outpath = indir + "/" + outdir

array = GetPathNames(outpath, ".utf8")


def GetOutputFileName(inputfilename):
	if (debug):
		outfilename = filename.lower().replace(".utf8", ".txt")
		print("Input File  is", filename)
		print("Output File is", outfilename)
	return outfilename


def GetInputStream(filename):
	i = open(filename, "r")
	return i


def GetOutputStream(filename):
	o = open(filename, "w")
	return o


def TransformText(filename):
	iname 	= filename
	f 	= GetInputStream(iname)
	oname 	= GetOutputFileName(filename)
	w 	= GetOutputStream(oname)
	if (debug):
		print("Transforming Text ...", end="", flush=True)
	for line in f:
		s = line.strip().lower()
		if (s.startswith("b'")):
			s = s[2:]
		if (s.endswith("'")):
			s = s[:-1]

		if (s.startswith('b"')):
			s = s[2:]
		if (s.endswith('"')):
			s = s[:-1]

		# approximation from utf8 to ascii
		for i in range(0, 5):
			s = s.replace("\\xe2\\x88\\x92", "a")	# A in Asutosa
			s = s.replace("\\xe2\\x80\\xa2", "A")
			s = s.replace("\\xe2\\x80\\xa6", "I")	# I in Isopanisad
			s = s.replace("\\xe2\\x80\\xa0", "a")	# a in radharani
			s = s.replace("\\xe2\\x80\\x9d", "i")

			s = s.replace("\\xe2\\x80\\x9e", "r")	# originally r
			s = s.replace("\\xe2\\x80\\x93", "t")
			s = s.replace("\\xe2\\x80\\x94", "S")	# S in KRSNA

			s = s.replace("\\xc5\\xa1",      " ")	# should probably be ""

			s = s.replace("\\xe2\\x80\\xb9", "m")
			s = s.replace("\\xe2\\x80\\x9a", "n")
			s = s.replace("\\xe2\\x80\\x9c", "s")	# s in Yasoda
			s = s.replace("\\xef\\xac\\x81", "n")
			s = s.replace("\\xe2\\x80\\xa1", "S")
			# ( k\xef\xac\x82\xc2\xa3\xe2\x80\xb0a , 2481 )
			s = s.replace("\\xef\\xac\\x82", "r")	# r in krsna
			s = s.replace("\\xc2\\xa3", 	 "s")	# s in krsna
			s = s.replace("\\xe2\\x80\\xb0", "n")	# n in krsna

			# ( xc2\xa5r\xc6\x92la , 340 )
			s = s.replace("\\xc2\\xa5", 	 "s")	# s in srila
			s = s.replace("\\xc6\\x92", 	 "i")	# i in srila

			# ( vedrnta-s\xc3\xa3tra , 83 )
			s = s.replace("\\xc3\\xa3", 	 "u")	# u in sutra

			# ( vaikun\xc3\xa0ha , 79 )
			s = s.replace("\\xc3\\xa0", 	 "t")	# t in vaikuntha
			# ( xc2\xa4ri-krsna-caitanya , 40 )
			s = s.replace("\\xc2\\xa4", 	 "s")	# s in sri

			# ( xc3\xa1hrkura , 372 )
			s = s.replace("\\xc3\\xa1", 	 "t")	# t in thakura

			# ( xe2\x80\x98svara , 29 )
			s = s.replace("\\xe2\\x80\\x98",  "i")	# i in isvara

			# ( brahma-sa\xe2\x80\xbahita , 20 )
			s = s.replace("\\xe2\\x80\\xba",  "i")	# m in samhita

			s = s.replace("\\xc5\\xb8",      "d")
			s = s.replace("\\xc5\\x81",      "n")

			s = s.replace("\\xc5\\x92",      "s")

			s = s.replace("\\xc4\\xb1",      "tTt")
			s = s.replace("\\xc3\\x95",      "'")
			s = s.replace("\\xc3\\x8c",      "A")	# A in Acarya
			s = s.replace("\\xc3\\xa8",      "N")	# N in KRSNA
			s = s.replace("\\xc3\\x91",      " - ")
			s = s.replace("\\xc3\\x92",      '"')	# open quotes
			s = s.replace("\\xc3\\x93",      '"')	# close quotes

			s = s.replace("\\xc2\\xb6",      ' ')	# reverse P in bible


			s = s.replace("\\'s", "'s")
			s = s.replace("\\'t", "'t")

			s = s.replace("\\n", " ")

			# ( tcarya , 412 )
			# ( pansita , 314 )
			# ( krsna--lord , 79 )
			s = s.replace("--", " ")

			s = s.lower()

			s = s.replace("krsnathe", "krsna the")
			s = s.replace("godheada", "godhead a")
			s = s.replace("canto.his", "canto his")
			s = s.replace("grace.a.c.", "grace a.c.")
			s = s.replace("gracea.c.", "grace a.c.")
			s = s.replace("consciousnessvolume", "consciousnss volume")
			s = s.replace("prabhupadafounder", "prabhupada founder")
			s = s.replace("visitwww.krishnapath.org", "visit www.krishnapath.org")
			s = s.replace(".text ", 	". text ")
			s = s.replace('."text ', 	". text ")
			s = s.replace(".translation ", 	". translation ") 
			s = s.replace("purport", 	" purport ")
			s = s.replace(".purport", 	". purport ")
			s = s.replace("bhagavad-gita", 	" bhagavad-gita ")

		print(s, file=w)
		print(" ", file=w)
	print("... Done")


for f in array:
	filename = f
	print(filename)
	TransformText(filename)
exit(0)
