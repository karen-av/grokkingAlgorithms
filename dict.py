s = set() 
set_1 = {1,2,3,4,8,6}
print(type(s), s)

d = dict()
dd = {}
print(type(d))
d['apple'] = 1.34
d['milk'] = 2.5
result = d.get('m')
print(result)

dict_names = {}
dict_names['Mike'] = True
dict_names['Jacke'] = True
name = input('That is your name? \n')
if dict_names.get(name):
    print('Get out!')
else:
    print("Let's do it!")
    dict_names[name] = True

print(dict_names)