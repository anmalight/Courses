f = open('001.txt', 'r')
d={}
for line in f:
	for symbol in line:

		if symbol not in d:
			d[symbol]=1
		else:
			d[symbol]+=1

for i in (sorted(val for key,val in d.items())):
    for key,val in d.items():
        if val==i:
            print(key + ': ' + str(val))

f.close()
