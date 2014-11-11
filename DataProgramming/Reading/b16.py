#!/usr/bin/env python

file = open("certificate.txt")
s = ""
for line in file:
	s = s + line

print(s)
