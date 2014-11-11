#!/usr/bin/env python
def indha(number):
	return number

def adutha(number):
	return 1+number

def bubble(ellamaanavargal):
	PositionMaathu = False
	MudhalThadava = True
	OrudhadavaMaathitomaa = False
	while OrudhadavaMaathitomaa or MudhalThadava:
		MudhalThadava = False
		OrudhadavaMaathitomaa = False
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

students = [ 1, 24, 16, 110, 11, 19, 18 ]
print(students)
bubble(students)
print(students)
exit(0)
