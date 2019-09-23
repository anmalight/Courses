a = [10,20,30,40]


for i in a:
	print(i)


for number, item in enumerate(a):
	a[number] = item + 5
print(a)


s = "This is a string we gonna iterate"
for symbol in  s[::3]:
	print(symbol)

print(s[0:len(s)])
print(len(s))
print(s[0:33])



s = "This is a string we gonna iterate"
lst = s.split()
for i in range(0, len(lst)):
	print(i)


import sys
filename = sys.argv[1]
f = open('001.txt', 'r')
for line in f:
	lst = line.split()
	for words in lst:
		print(words)

f.close()



# Словари
d = {}
d['a'] = 5
for key in d:
	print(d[key])
print(d)

f = open('001.txt', 'r')
d={}
for line in f:
	for symbol in line:

		if symbol not in d:
			d[symbol]=1
		else:
			d[symbol]+=1
print(d)


f.close()
