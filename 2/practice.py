# -*- coding: utf-8 -*-

# Проверить, является ли введеное число четным.
input_nunber = int(input("Enter number: "))
if not input_nunber%2: #not иначе 0 - False
    print('even')
else:
    print('not even')


# Проверить, является ли число нечетным, делится ли на три и на пять одновременно, но так, чтобы не делиться на 10.
x = int(input("Enter number: "))
if (x%2 == 1 and x%3 == 0 and x%5 == 0 and x%10 !=0):
    print('Y')


# Ввести число, вывести все его делители
number = int(input("Enter number: "))
i = 1
while i <= number:
	if number%i == 0:
		print(i)
	i += 1


# Ввести число, вывести его разряды и их множители.
number = int(input("Enter number: "))
number = abs(number)
l = str(number)

count = 0
number //= 10
while number > 0:
    number //= 10
    count += 1

final_l = []
for i in l:
    # print(i)
    res = i + ' * 10 ** ' + str(count)
    count -= 1
    final_l.append(res)
final_s = ' + '.join(final_l)

print(final_s.lstrip('+'))
