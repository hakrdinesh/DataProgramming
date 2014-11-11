#!/usr/bin/env python

def bubble(a):
	sorted = False
	while not sorted:
		sorted = True	# assume it is sorted
		n = 0
		for s in a[0:-1]:
			left  = a[ n   ]
			right = a[ n+1 ]
			if (left > right):
				a[ n   ] = right
				a[ n+1 ] = left
				sorted = False	# we swapped, so not sorted
			n = n + 1

students = [ 1, 24, 16, 110, 11, 19, 18 ]
print(students)
bubble(students)
print(students)
exit(0)
