#!/usr/bin/env python

debug = False

file = open("certificate.txt")
otext = ""
for line in file:
	otext = otext + line

text = otext

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
	print("Date:", date_of_visit)
	print("")

	print("To:")
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

	print(salutation, fullname)

	course = certificate["COURSE"]
	if (course == "MT"):
		print("M.Tech. Student")
	
	department = certificate["DEPARTMENT"]
	if (department == "CSE"):
		print("Department of ", end="")
		print("Computer Science and Engineering")
	
	elif (department == "SE"):
		print("Department of ", end="")
		print("Software Engineering")

	elif (department == "DB"):
		print("Department of ", end="")
		print("Database Systems")

	else:
		# unknown department
		pass # keep quiet, carry on

	college = certificate["COLLEGE"]
	if (college == "IIITS"):
		print("Indian Institute of Information Technology, Srirangam")

	elif (college == "GCES"):
		print("Government College of Engineering, Srirangam")
	
	else:
		print(college)

	text = otext
	text = text.replace("FULLNAME", fullname)
	text = text.replace("SALUTATION", salutation)
	text = text.replace("DATE", date_of_visit)
	text = text.replace("HE_OR_SHE", he_or_she)
	text = text.replace("HIM_OR_HER", him_or_her)
	text = text.replace("HIS_OR_HER", his_or_her)

	print(text)

