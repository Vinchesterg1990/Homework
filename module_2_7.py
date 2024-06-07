def print_params (a = 1, b = 'Иван', c = True):
    print(a, b, c)


values_list = [33, 'Евгения', [9,12]]
values_dict = {'a': 15, 'b' : 'Сергей', 'c'  : [19,49]}
values_list_2 = [54.32, 'Победа']

print_params()
print_params(b=25)
print_params(c=[1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)

