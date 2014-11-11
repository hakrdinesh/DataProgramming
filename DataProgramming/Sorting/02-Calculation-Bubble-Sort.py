#!/usr/bin/env python
import copy

def indha(number):
	return number

def adutha(number):
	return 1+number

def bubble_calculation(ellamaanavargal):
	PositionMaathu = False
	number = 0
	for ovorumaanavan in ellamaanavargal[0:-1]:

		print("Ippo ...")
		print(ellamaanavargal)
		indhamaanavan  = ellamaanavargal[ indha  (number) ]
		print("Indha Maanavan  =", indhamaanavan)

		aduthamaanavan = ellamaanavargal[ adutha (number) ] 
		print("Adutha Maanavan =", aduthamaanavan)

		print("")
		print("Edai Podu", indhamaanavan, aduthamaanavan)

		if (indhamaanavan < aduthamaanavan):
			print("<	so okay")
			print("\tOrder sariyaa irukudhu")
	
		if (indhamaanavan == aduthamaanavan):
			print("=	still okay")
			print("\tOrder sariyaavum irukudhu")
			
		if (indhamaanavan > aduthamaanavan):
			PositionMaathu = True
			print(">	not okay, so maathu idam")

			print("\tOrder Maathaporom")
			print("\t", ellamaanavargal)
			ellamaanavargal[ indha  (number) ] = aduthamaanavan
			ellamaanavargal[ adutha (number) ] = indhamaanavan
			print("\tOrder Maathiyaachu")
			OrudhadavaMaathitomaa = True
			print("\t", ellamaanavargal)

		number = adutha(number)
		print("Aduthathu paarkalam")
		print("")

	if (OrudhadavaMaathitomaa):
		print("OrudhadavaMaathitomaa is", OrudhadavaMaathitomaa)
		print("Appadi enral, thiruppi pannum")
	else:
		print("OrudhadavaMaathitomaa is", OrudhadavaMaathitomaa)
		print("Appadi enral, thiruppi panna thevai illai")

students = [ 90, 14, 16, 99, 11, 19, 18 ]
original = copy.copy(students)
print(original)
print(students)
bubbleonce(students)
print(original)
print(students)
exit(0)
