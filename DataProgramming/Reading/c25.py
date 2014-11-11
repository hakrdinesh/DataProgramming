#!/usr/bin/env python

import os
import sys

debug = False
allInOne = True
nEmptyLines = 4

file = open("certificate.txt")
otext = ""
for line in file:
	otext = otext + line

text = otext
w = None	# output file handle

file = open("students.csv")
for line in file:
	l = line.strip()
	if (debug):
		print("DEBUG: ", l)
	student = l.split(",")
	if (debug):
		print(student)

	record = {}

	keys = ( "FULLNAME", "GENDER", "COURSE", "DEPARTMENT", "COLLEGE", "DATE_OF_VISIT" )


	certificate = {}
	k = 0
	for key in keys:
		value = student[k]
		certificate[key] = value.strip()
		k += 1

	for key in certificate.keys():
		if (debug):
			print(key, certificate[key])


	date_of_visit = certificate["DATE_OF_VISIT"]

	header = "\n" * nEmptyLines
	header += "Date: " + date_of_visit + "\n"
	header += "\n"

	header += "To:" + "\n"
	fullname = certificate["FULLNAME"]

	gender = certificate["GENDER"]

	if (gender == "Male"):
		salutation = "Mr."
		he_or_she = "He"
		him_or_her = "him"
		his_or_her = "his"
	else:
		salutation = "Ms."
		he_or_she = "She"
		him_or_her = "her"
		his_or_her = "her"

	header += salutation + " " + fullname + ",\n"

	course = certificate["COURSE"]
	if (course == "MT"):
		header += "M.Tech. Student" + ",\n"
	
	department = certificate["DEPARTMENT"]
	if (department == "CSE"):
		header += "Department of " + "Computer Science and Engineering" + ",\n"
	
	elif (department == "SE"):
		header += "Department of " + "Software Engineering" + ",\n"

	elif (department == "DB"):
		header += "Department of " + "Database Systems" + ",\n"

	else:
		# unknown department
		pass # keep quiet, carry on

	college = certificate["COLLEGE"]
	if (college == "IIITS"):
		header += "Indian Institute of Information Technology, Srirangam" + "\n"

	elif (college == "GCES"):
		header += "Government College of Engineering, Srirangam"
	
	else:
		header += college

	text = otext
	text = text.replace("FULLNAME", fullname)
	text = text.replace("SALUTATION", salutation)
	text = text.replace("DATE", date_of_visit)
	text = text.replace("HE_OR_SHE", he_or_she)
	text = text.replace("HIM_OR_HER", him_or_her)
	text = text.replace("HIS_OR_HER", his_or_her)

	if (allInOne):
		# open output file only once
		ofilename = "output/output.txt"
		if (w == None):
			w = open(ofilename, "w")
			print("Once Filename:", ofilename, file=sys.stderr)
			
	else:
		# open output file for every student
		ofilename = "output/" + fullname.replace(" ", "_") + ".txt"
		w = open(ofilename, "w")
		print("Filename:", ofilename, file=sys.stderr)

	print(header, file=w, flush=True)
	print(text, file=w, flush=True)

	# All certificates in 1 file, separated by formfeed
	if (allInOne):
		print("\f", file=w, flush=True)


