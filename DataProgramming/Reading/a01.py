#!/usr/bin/env python

file = open("students.csv")
for line in file :
	copy = line.strip()
	print(copy)
