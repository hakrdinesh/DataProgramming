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
	for key in keys:
		print(key)
		value = student[k]
		value = value.strip()
		print(value)
		k += 1

