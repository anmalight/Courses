# 1
# Написать 2 функции. Первая функция будет принимать строку и приводить ее к
# нижнему регистру.
# Вторая функция будет принимать строку и проводить ее к верхнему регистру.
# После чего с помощью map применить ваши функции к списку строк. Отдельно каждую
# функцию к отдельному списку строк!
def upper_func(vvod):
	return vvod.upper()

def lower_func(vvod):
	return vvod.lower()

v1 = lower_func(input())
v2 = upper_func(input())
print(v1)
print(v2)


s1=['kjdKJGhg', 'KJJUGlh']
s2=['kjdKJGhg', 'KJJUGlh']

map1 = list(map(upper_func,s1))
map2 = list(map(lower_func,s2))
print(map1)
print(map2)


# 2
# Написать функцию которая будет простое число возводить в квардрат.
# Необходимо возвести в квадрат все простые числа в списке используя функцию map
def squared(n):
	return n**2

def prime(num):
	for i in range(2,num):
		if (num % i) == 0:
			no = str(num)+" is not a prime number"
			return 1
			break
	else:
		return num

our_list = [1, 2, 8, 78, 12, 113]

map3 = list(map(prime, our_list))
map4 = list(map(squared,map3))
# print(map3)
print(map4)


# 3
# Есть файл, в котором много англоязычных текстовых строк. Считаем частоту
# встретившихся слов в файле, но через функции и map, без единого циклa
with open('filename2.txt', 'r') as file:
    def frequency(words):
        words = file.read().lower().split()
        a_l = list(set(words))
        freq_list = [words.count(x) for x in a_l]
        ord_freq_lists =  list(zip(a_l,sorted(freq_list)))
        return ord_freq_lists

    print(list(map(frequency, file)))
