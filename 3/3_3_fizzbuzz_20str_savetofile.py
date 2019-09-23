f = open('filename.txt', 'r')
list_to_print = []
for line in f:
	t_list = line.split()
	fizz = int(t_list[0])
	buzz = int(t_list[1])
	to_check = int(t_list[2])

	list_to_print = []
	list_to_write = []
	for i in range(1, to_check+1):
		if(i%fizz==0 and i%buzz==0):
			list_to_print.append("fb")
		elif (i%fizz==0):
			list_to_print.append("f")
		elif (i%buzz==0):
			list_to_print.append("b")

		else:
			list_to_print.append(i)
		list_to_write = []
		list_to_write.append(list_to_print)
		srt_list_to_write = ''

	t_file = open('text.txt', 'a')#

	for item in list_to_write:
		for ii in item:
			srt_list_to_write += str(ii) + ' '

		t_file.write(srt_list_to_write)
		t_file.write('\n')


	t_file.close()

f.close()
