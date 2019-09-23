# -*- coding: utf-8 -*-

# 1
# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента). Найти самого успешного и самого отстающего по среднему баллу.
# Работает
'''
group_dict = {'Ivan Ivanov': [3, 4, 4, 5], 'Anna V': [4, 3, 3, 5], 'Inga Shi' : [3, 3, 3, 3], 'Peter Petroff': [5, 4, 5, 5]}

def max_min_marks(dictionary):
	d = {}
	for key, value in group_dict.items():
		z = sum(value)/len(value)
		d[key] = z

	maximum = max(d, key=d.get)
	minimum = min(d, key=d.get)
	s_min = (maximum, d[maximum])
	s_max = (minimum, d[minimum])

	return s_min, s_max


print(max_min_marks(group_dict))



#Напишите функцию перевода размеров одежды из международного во все остальные. Внтри функции нужно просто обращаться к правильно составленному словарю.
# calculator = {
#     'plus': lambda x, y: x + y,
#     'minus': lambda x, y: x - y,
#     'mul': lambda x, y: x*y,
#     'div': lambda x, y: x/y,
#     'mod': lambda x, y: x%y
# }
# print(calculator['minus'](9,3))


verh_odezhda = {
	's':{
	'Russia':40,
	'Belgium, Germany, the Netherlands, Norway, Finland, Sweden': 34,
	'France, Sweden': 36,
	'Italy':38,
	'Great Britain':8,
	'USA': 6
	},

	'm':{
	'Russia':42,
	'Belgium, Germany, the Netherlands, Norway, Finland, Sweden': 36,
	'France, Sweden': 38,
	'Italy':40,
	'Great Britain':10,
	'USA': 8
	},

	'l':{
	'Russia':46,
	'Belgium, Germany, the Netherlands, Norway, Finland, Sweden': 40,
	'France, Sweden': 42,
	'Italy':44,
	'Great Britain':14,
	'USA': 12
	},

	'xl':{
	'Russia':50,
	'Belgium, Germany, the Netherlands, Norway, Finland, Sweden': 44,
	'France, Sweden': 46,
	'Italy':48,
	'Great Britain':18,
	'USA': 16
	},


	'xxl':{
	'Russia':54,
	'Belgium, Germany, the Netherlands, Norway, Finland, Sweden': 48,
	'France, Sweden': 50,
	'Italy':52,
	'Great Britain':22,
	'USA': 20
	}
}



def find_c_size(inter_size, country_name):
	# verh_odezhda
	for  key,value in verh_odezhda.items():
		if key == inter_size:
			# return value
			for k, v in (value.items()):
				if k == country_name:
					# print(v)
					return v

print(find_c_size("xl", "Italy"))
