
import sys

file_name = sys.argv[1]
file = open(file_name, 'r')
for line in file:
	print(line, end = '')
file.close()
