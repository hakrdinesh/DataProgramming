#!/usr/bin/env python

file = open("students.csv")
for line in file:
	l = line.strip()
	print("DEBUG: ", l)
	student = l.split(",")
	print(student)

	record = {}

	keys = ( "FULLNAME", "GENDER", "COURSE", "DEPARTMENT_CODE", "COLLEGE", "DATE_OF_VISIT" )

	for key in keys:
		print(key)


