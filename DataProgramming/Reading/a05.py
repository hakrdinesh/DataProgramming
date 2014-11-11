#!/usr/bin/env python

file = open("students.csv")
for line in file:
	l = line.strip()
	print("DEBUG: ", l)
	student = l.split(",")
	print(student)

	record = {}

	key = "FULLNAME"
	value = student[0]
	record[key] = value
	print(key, "is", value)
	print(key, "is", record[key])

	key = "GENDER"
	value = student[1]
	record[key] = value
	print(key, "is", value)
	print(key, "is", record[key])

	key = "COURSE"
	value = student[2]
	record[key] = value
	print(key, "is", value)
	print(key, "is", record[key])

	key = "DEPARTMENT_CODE"
	value = student[3]
	record[key] = value
	print(key, "is", value)
	print(key, "is", record[key])

	key = "COLLEGE"
	value = student[4]
	record[key] = value
	print(key, "is", value)
	print(key, "is", record[key])

	key = "DATE_OF_VISIT"
	value = student[5]
	record[key] = value
	print(key, "is", value)
	print(key, "is", record[key])

