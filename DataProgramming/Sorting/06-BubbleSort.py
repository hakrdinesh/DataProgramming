#!/usr/bin/env python

def bubble(a):
	first = True
	swapped = False

	while swapped or first:

		first = False
		swapped = False

		n = 0
		for s in a[0:-1]:

			left  = a[ n ]
			right  = a[ 1+n ]

			if (left > right):
				a[ n] = right
				a[ n+1 ] = left
				swapped = True

			n = n + 1


students = [ 1, 24, 16, 110, 11, 19, 18 ]
print(students)
bubble(students)
print(students)
exit(0)
