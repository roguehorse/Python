#!/usr/bin/python
#squaring_1
#from CodeAcademy tutorial
#Scott DuBois
#10/3/2014

start_list = [5, 3, 1, 2, 4]
square_list = []

for numbers in start_list:
	numbers = (numbers ** 2)
	square_list.append(numbers)

square_list.sort()

print square_list


