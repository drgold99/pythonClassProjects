import csv

file1 = open('us_postal_codes.csv', 'r')
Lines = file1.readlines()

for l in Lines:
	print (l)
	a = l.split(',')
	b= a[0]
	print (b)
	