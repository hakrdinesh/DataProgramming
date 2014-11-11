#!/usr/bin/env python

file = open("students.csv")
for line in file:
	l = line.strip()
	print("DEBUG: ", l)
	student = l.split(",")
	print(student)

	record = {}

	keys = ( "FULLNAME", "GENDER", "COURSE", "DEPARTMENT_CODE", "COLLEGE", "DATE_OF_VISIT" )

	k = 0
	for p in keys:
		print(p)
		value = student[k]
		print(value)
		k += 1


