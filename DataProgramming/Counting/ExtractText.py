#!/usr/bin/env python
# pdf to ascii conversion

from __future__ import print_function

import os
import sys
import PyPDF2

debug		= True
testing 	= True
alwaysExtract 	= True

outdir 		= "output"
suffix 		= ".pdf"

if (testing):
	indir = "Books"
else:
	indir = "../../../DataSetForLIFE"

def GetPDFPathNames(indir):
	pathnames = []
	for (dir, subdirs, files) in os.walk(indir):
		if (debug):
			print("Root Directory", indir, file=sys.stderr)
			print("Subdirectories", subdirs, file=sys.stderr)
			print("Files         ", files, file=sys.stderr)
		for d in subdirs:
			print("Subdirectory  ", d, file=sys.stderr)
		for f in files:
			if f.lower().endswith(".pdf"):
				if ("scan" in f.lower()):
					print("Scanned PDF  - ", f, file=sys.stderr)
				else:
					print("PDF File     + ", f, file=sys.stderr)
					pathname = dir + "/" + f
					print("PDF Path     + ", pathname, file=sys.stderr)
					pathnames.append(pathname)
			else:
				print("Regular File - ", f, file=sys.stderr)
	print("DEBUG: PDF Pathnames", pathnames)
	return pathnames


def GetOutputFileName(inpath):
	components = inpath.strip().split("/")
	inlast = components.pop()
	outlast = inlast.replace(".pdf", ".utf8")
	if not testing:
		components.append(outdir)
	components.append(outlast)
	outpath = "/".join(components)
	if (debug):
		print("Input File  is", inpath)
		print("Output Path Components:", components)
		print("Output File is", outpath)
	return outpath

def GetInputStream(filename):
	try:
		i = PyPDF2.PdfFileReader(open(filename, "rb"))
		return i
	except:
		i = None
		print("ERROR: Unable to open a PDF Reader on", filename, file=sys.stderr, flush=True)
	return i

def GetOutputStream(filename):
	o = open(filename, "w")
	return o

def GetBaseDirectory(pathname):
	f = pathname.strip().split("/")
	f.pop()
	d = "/".join(f)
	print("DEBUG: GetBaseDirectory", d)
	return d

def ExtractText(filename):
	iname 	= filename
	f 	= GetInputStream(iname)
	if (f == None):
		return

	oname 	= GetOutputFileName(filename)
	if os.path.exists(oname):
		if os.path.isfile(oname):
			if not alwaysExtract:
				print("SKIP: UTF8 Extracted File is already present", oname, file=sys.stderr, flush=True)
				return
	else:
		basedir = GetBaseDirectory(oname)

	w = GetOutputStream(oname)

	if (f.isEncrypted):
		if (debug):
			print("DEBUG:", filename, "is encrypted", file=sys.stderr)
		try:
			rv = f.decrypt("")
			if (debug):
				print("DEBUG: decryption return value is ", rv, file=sys.stderr)
			if (rv == 0):
				print("ERROR: decryption failed, so exit", file=sys.stderr)
				exit(1)
		except:
			print("ERROR: Failed to decrypt", filename, file=sys.stderr)
			return 0

	npages = f.getNumPages()
	for p in range(0, npages):	# iterate over all pages
		page = f.getPage(p)		# get the page
		try:
			text = page.extractText()	# extract text
			string = text.encode("utf-8")	# get printable string
			print(string, file=w)
			if (debug):
				print("Extracted Text from Page", p, "of", npages, "from", iname, "to", oname, file=sys.stderr)
		except:
			print("Warning: Failed to Extracted Text from Page", p, "of", npages, "from", iname, "to", oname, file=sys.stderr)

def FileIsToBeRejected(filename):
	if "letters_from_srila" in filename.lower():
		return True
	if "sb-canto" in filename.lower():
		return True
	if "kunti" in filename.lower():
		return True
	if "the-nectar-of-instruction" in filename.lower():
		return True
	if "transcendental_teachings" in filename.lower():
		return True
	if "the_krishna_consciousness_handbook" in filename.lower():
		return True
	if "prospectus" in filename.lower():
		return True
	if "on_chanting" in filename.lower():
		return True
	if "easy_journy" in filename.lower():
		return True
	if filename.lower().startswith("sb-"):
		return True
	return False

array = GetPDFPathNames(indir)
for f in array:
	print(f)
	if (FileIsToBeRejected(f)):
		print("DEBUG: Skipping Reject File", f, file=sys.stderr)
		continue
	ExtractText(f)
exit(0)
