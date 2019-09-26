# For 2 only
# def custome_zip_2lists(s,t):
# 	lists_min_len = range(min(len(s),len(t)))
# 	return [(s[i], t[i]) for i in lists_min_len]
#
# s1 = [2, 8, 14, 90, 78]
# t1 = [10, 20, 30, 7]
#
# print(custome_zip_2lists(s1,t1))

# For more 
def custome_prezip(*args):
    return tuple(args)

def custome_zip_list(custome_prezip,*args):
    return list(map(custome_prezip,*args))
def custome_zip_tuple(custome_prezip,*args):
    return tuple(map(custome_prezip,*args))
def custome_zip_set(custome_prezip,*args):
    return set(map(custome_prezip,*args))


j1 = (1, 2, 3)
j2 = (4,5,6,10)
j3 = (7,8,9,)
print(custome_zip_list(custome_prezip, j1, j2, j3))
print(custome_zip_tuple(custome_prezip, j1, j2, j3))
print(custome_zip_set(custome_prezip, j1, j2, j3))


# def list_zip(*args):
#     return tuple(args)
#
# print(list(map(list_zip, j1, j2, j3)))
# print(tuple(map(list_zip, j1, j2, j3)))
