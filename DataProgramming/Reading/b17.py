#!/usr/bin/env python

file = open("certificate.txt")
text = ""
for line in file:
	text = text + line

text = text.replace("FULLNAME", 	"Jai Narasimha")
text = text.replace("SALUTATION", 	"Mr.")
text = text.replace("DATE", 		"15-08-1972")
text = text.replace("HE_OR_SHE", 	"He")
text = text.replace("HIM_OR_HER", 	"him")
text = text.replace("HIS_OR_HER", 	"his")

print(text)

