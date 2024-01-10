def print_params(a=1, b='строка', c=True):
    print("Значение параметра a:", a)
    print("Значение параметра b:", b)
    print("Значение параметра c:", c)
print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list = [5, 'текст', False]
values_dict = {'a': 5, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['другой текст', 100]
print_params(*values_list_2,42)