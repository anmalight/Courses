fizz = int(input("Введите fizz число:"))
buzz = int(input("Введите buzz число:"))
l_number = int(input("Введите предельное число:"))

list_to_print = []

for i in range(1, l_number+1):

	if (i%fizz==0 and i%buzz==0):
		list_to_print.append("fb")
	elif (i%fizz==0):
		list_to_print.append("f")
	elif (i%buzz==0):
		list_to_print.append("b")

	else:
		list_to_print.append(i)


for j in list_to_print:
	print(j, end=" ")
