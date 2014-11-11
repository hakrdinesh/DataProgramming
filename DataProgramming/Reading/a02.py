#!/usr/bin/env python

file = open("students.csv")
for line in file:
	l = line.strip()
	print("DEBUG: ", l)
