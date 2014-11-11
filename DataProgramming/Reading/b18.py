#!/usr/bin/env python

file = open("certificate.txt")
otext = ""
for line in file:
	otext = otext + line


ntext = otext
ntext = ntext.replace("FULLNAME", "Gopal Bhattar")
ntext = ntext.replace("SALUTATION", "Mr.")
ntext = ntext.replace("DATE", "11-11-2014")
ntext = ntext.replace("HE_OR_SHE", "He")
ntext = ntext.replace("HIM_OR_HER", "him")
ntext = ntext.replace("HIS_OR_HER", "his")
print(ntext)

ntext = otext
ntext = ntext.replace("FULLNAME", "Jai Narasimha")
ntext = ntext.replace("SALUTATION", "Mr.")
ntext = ntext.replace("DATE", "11-11-2014")
ntext = ntext.replace("HE_OR_SHE", "He")
ntext = ntext.replace("HIM_OR_HER", "him")
ntext = ntext.replace("HIS_OR_HER", "his")
print(ntext)

