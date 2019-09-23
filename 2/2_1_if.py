# -*- coding: utf-8 -*-

#example of if-elif-else
print("Give it to me!")
number = int(input())

if (number>=100):
	print("Thanks, human!")
elif((number > 10) and (number < 100)):
	print("OK :(")
else:
	print("Whaat?")

if (number > 1000):
	print("!!!WOOWW!!!")


#example of code similar to the ternal operator
test = True
result = 'Test is True' if test else 'Test is False'
print(result)
#result = 'Test is True!'
test = []
result = 'Test is True' if test else 'Test is False'
print(result)
#result = 'Test is False!'

#example of code similar to the ternal operator
test = True
print('ttt' if test else 'fff')
#result = 'ttt'


# Features of object comparison
s = ''
if s !='':
	pass
if 8 % 2 != 0:
	pass
#we can cut
if s:
	pass
if 8%2:
	pass

#Another alternative to ternary operator
'''Применение and к нескольким выражениям не просто возвращает True или False.
Оно возвращает первое false-выражение, либо последнее из выражений, если все они true.'''
a = 11
if a > 10 and a < 20:
	pass

'''В нашем случае test = True, т.е. and его пропускает и возвращает нам последнее из истинных
значений, с которым работал, т.е. выражение 'Test is True' or 'Test is False'. Or возвращает

первое встреченное true выражение, ему больше ничего не интересно.
'''
test = 8 #True
result = test  and 'Test is True' or 'Test is False'
print(result)
