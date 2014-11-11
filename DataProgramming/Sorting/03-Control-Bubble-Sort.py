#!/usr/bin/env python

import copy

def indha(number):
	return number

def adutha(number):
	return 1+number

def computation(ellamaanavargal):
	PositionMaathu = False
	EdhavadhuMaathinomaa = False
	number = 0
	for ovorumaanavan in ellamaanavargal[0:-1]:

		print("\tIppo ...")
		print("\t", ellamaanavargal)
		indhamaanavan  = ellamaanavargal[ indha  (number) ]
		print("\tIndha Maanavan  =", indhamaanavan)

		aduthamaanavan = ellamaanavargal[ adutha (number) ] 
		print("\tAdutha Maanavan =", aduthamaanavan)

		print("")
		print("\tEdai Podu", indhamaanavan, aduthamaanavan)

		if (indhamaanavan < aduthamaanavan):
			print("\t<	so okay")
			print("\t\tOrder sariyaa irukudhu")
	
		if (indhamaanavan == aduthamaanavan):
			print("\t=	still okay")
			print("\t\tOrder sariyaavum irukudhu")
			
		if (indhamaanavan > aduthamaanavan):
			PositionMaathu = True
			print("\t>	not okay, so maathu idam")

			print("\t\tOrder Maathaporom")
			print("\t\t\t", ellamaanavargal)
			ellamaanavargal[ indha  (number) ] = aduthamaanavan
			ellamaanavargal[ adutha (number) ] = indhamaanavan
			print("\t\tOrder Maathiyaachu")
			EdhavadhuMaathinomaa = True
			print("\t\t\t", ellamaanavargal)

		number = adutha(number)
		print("\tAduthathu paarkalam")
		print("")

	if (EdhavadhuMaathinomaa):
		print("EdhavadhuMaathinomaa is", EdhavadhuMaathinomaa)
		print("Appadi enral, thiruppi pannum")
	else:
		print("EdhavadhuMaathinomaa is", EdhavadhuMaathinomaa)
		print("Appadi enral, thiruppi panna thevai illai")

	return EdhavadhuMaathinomaa


def control(ellamaanavargal):
	PositionMaathu = False
	MudhalThadava = True
	Maathindirukirom = False
	while Maathindirukirom or MudhalThadava:
		MudhalThadava = False
		Maathindirukirom = computation(ellamaanavargal)
		if (Maathindirukirom):
			print("Maathindirukirom is", Maathindirukirom)
			print("Appadi enral, thiruppi pannum")
		else:
			print("Maathindirukirom is", Maathindirukirom)
			print("Appadi enral, thiruppi panna thevai illai")

students = [ 90, 14, 16, 99, 11, 19, 18 ]

def bubblesort(data):
	control(data)

original = [ 90, 14, 16, 22, 11 ]
print(original)
students = copy.copy(original)
print(students)

bubblesort(students)

print(original)
print(students)

exit(0)
