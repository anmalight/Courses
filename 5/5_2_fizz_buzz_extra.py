f = open('filename.txt').readlines()


# Выдаст список строчных значений физз из док-та
def fizz_list(string):
	return [line.split(' ', 1)[0] for line in string]

# Выдаст список строчных значений базз из док-та
def buzz_list(string):
	return [line.split(' ', 2)[1] for line in string]

# Выдаст список строчных значений числа, для которого находим физз и базз
def to_check_list(string):
	t_l = [line.split(' ', 3)[2] for line in string]
	return [item.rstrip() for item in t_l]


# Выдаст списк со спиками по каждой пройденой тройке цифр
def fizzbuzz(fizz, buzz, numbers):
	x = ['fb' if x % int(fizz) == 0 and x % int(buzz) == 0 else 'f' if x % int(fizz) == 0 else 'b' if x % int(buzz) == 0 else x for x in range(1, int(numbers)+1)]
	return x


results = list(map(fizzbuzz, fizz_list(f), buzz_list(f), to_check_list(f)))

print(results)

# для красивого вывода построчно
srt_list_to_write=''
for item in results:
	for ii in item:
		srt_list_to_write += str(ii) + ' '
	srt_list_to_write += '\n'
print(srt_list_to_write)
