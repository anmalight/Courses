
import sys
file_name_list=[]
for args in sys.argv:
	file_name_list.append(args)
file_name_list.pop(0)
print(file_name_list)

for f_n_l in file_name_list:
	file = open(f_n_l, 'r')
	for line in file:
		print(line, end = '')
	file.close()
