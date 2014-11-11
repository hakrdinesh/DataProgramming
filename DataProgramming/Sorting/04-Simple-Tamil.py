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

			indhamaanavan  = ellamaanavargal[ indha  (number) ]

			aduthamaanavan = ellamaanavargal[ adutha (number) ] 


			if (indhamaanavan < aduthamaanavan):
		
			if (indhamaanavan == aduthamaanavan):
				print("\tOrder sariyaavum irukudhu")
				
			if (indhamaanavan > aduthamaanavan):
				PositionMaathu = True

				ellamaanavargal[ indha  (number) ] = aduthamaanavan
				ellamaanavargal[ adutha (number) ] = indhamaanavan
				OrudhadavaMaathitomaa = True

			number = adutha(number)


students = [ 1, 24, 16, 110, 11, 19, 18 ]
print(students)
bubble(students)
print(students)
exit(0)
