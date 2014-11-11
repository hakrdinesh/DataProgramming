#!/usr/bin/env python

file = open("students.csv")
for line in file:
	l = line.strip()
	print("DEBUG: ", l)
	student = l.split(",")
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
		print(key, certificate[key])


	fullname = certificate["FULLNAME"]
	gender = certificate["GENDER"]

	if (gender == "Male"):
		print("Mr.", fullname)
	else:
		print("Ms.", fullname)

	course = certificate["COURSE"]
	if (course == "MT"):
		print("M.Tech. Student")
	
	department = certificate["DEPARTMENT"]
	if (department == "CSE"):
		print("Computer Science and Engineering")
	
	if (department == "SE"):
		print("Software Engineering")

	college = certificate["COLLEGE"]
	if (college == "IIITS"):
		print("Indian Institute of Information Technology, Srirangam")

	elif (college == "GCES"):
		print("Government College of Engineering, Srirangam")
	
	else:
		print(college)



