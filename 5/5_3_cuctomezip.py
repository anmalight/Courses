def custome_zip_2lists(s,t):
	lists_min_len = range(min(len(s),len(t)))
	return [(s[i], t[i]) for i in lists_min_len]

s1 = [2, 8, 14, 90, 78]
t1 = [10, 20, 30, 7]

print(custome_zip_2lists(s1,t1))
