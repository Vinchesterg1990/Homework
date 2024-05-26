my_dict = {'Anastasia': 2012, 'Sergey': 2014, 'Evgenia': 1991}
print(my_dict)
print(my_dict['Anastasia'])
print(my_dict.get('Ivan'))
my_dict.update({'Nina': 1964, 'Vasiliy': 1973})
a = my_dict['Sergey']
del my_dict ['Sergey']
print(a)
print(my_dict)
my_set = { 1990,1990, 1991,2012, 2012,2014,1991,'Elena','Ivan','Evgenia'}
print(my_set)
print(my_set.add('Sergey'))
print(my_set.add('Anastasia'))
print(my_set.remove('Elena'))
print(my_set)
