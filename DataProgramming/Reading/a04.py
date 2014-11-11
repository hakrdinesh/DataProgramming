#!/usr/bin/env python

file = open("students.csv")
for line in file:
	l = line.strip()
	print("DEBUG: ", l)
	student = l.split(",")
	print(student)

	print("FULLNAME        is ", student[0])
	print("GENDER          is ", student[1])
	print("COURSE          is ", student[2])
	print("DEPARTMENT_CODE is ", student[3])
	print("COLLEGE         is ", student[4])
	print("DATE_OF_VISIT   is ", student[5])
