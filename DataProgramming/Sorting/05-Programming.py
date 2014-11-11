#!/usr/bin/env python

def bubble(a):
	first = True
	swapped = False

	while swapped or first:

		first = False
		swapped = False
		n = 0

		# for ovorumaanavan in ellamaanavargal[0:-1]:
		for s in a[0:-1]:

			# indhamaanavan  = ellamaanavargal[ indha  (number) ]
			left  = a[ n ]

			# aduthamaanavan = ellamaanavargal[ adutha (number) ] 
			right  = a[ 1+n ]

			# if (indhamaanavan > aduthamaanavan):
			if (left > right):

				a[ n] = right
				a[ n+1 ] = left
				# OrudhadavaMaathitomaa = True
				swapped = True

			# number = adutha(number)
			n = n + 1


students = [ 1, 24, 16, 110, 11, 19, 18 ]
print(students)
bubble(students)
print(students)
exit(0)
