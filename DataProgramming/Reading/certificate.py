#!/usr/bin/env python
from __future__ import print_function

import os
import sys


debug = False
allInOne = False
nEmptyLines = 4

file = open("certificate.txt")
otext = ""
for line in file:
	otext = otext + line

text = otext
w = None	# output file handle

department_counts = {}
attended = {}

def ExpandedDepartmentName(s):
	if (s == "CSE"):
		return "Computer Science and Engineering"
	elif (s == "SE"):
		return "Software Engineering"
	elif (s == "DB"):
		return "Database Systems"
	# unknown department, return the same string
	return s

file = open("students.csv")
for line in file:
	l = line.strip()
	if (debug or True):
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
	department_full_name = ExpandedDepartmentName(department)
	header += "Department of " + department_full_name + ",\n"

	# update count for the department seen
	if (department in department_counts.keys()):
		n = 1+int(department_counts[department])
		department_counts[department] = str(n)
	else:
		n = 1
		department_counts[department] = str(n)
	if (debug):
		print("DEBUG: So far seen", n, department, "students")

	if department in attended.keys():
		value = attended[department]
		namelist = value.split(",")
	else:
		value = ""
		namelist = []

	namelist.append(fullname)
	print(namelist)
	value = ",".join(namelist)
	attended[department] = value
	print("DEBUG: attended namelist for ", department, "is", namelist)

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

	print(header, file=w)
	print(text, file=w)

	# All certificates in 1 file, separated by formfeed
	if (allInOne):
		print("\f", file=w)


print("Summary")
dlist = list(department_counts.keys())
print("DEBUG: dlist", dlist)
dlist.sort()
print("DEBUG: dlist", dlist)
for d in dlist:
	n = department_counts[d]
	print("Department", d, ":", n, "students")

for d in dlist:
	department_full_name = ExpandedDepartmentName(d)
	print("Department of", department_full_name)

	value = attended[d]
	slist = value.split(",")
	i = 1
	for student in slist:
		print(i, ".", student)
		i += 1

	print("\n")
