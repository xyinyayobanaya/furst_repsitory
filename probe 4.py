def func_with_params(param):
    print('Функция вызвана с параметром', param)

my_list = [3, 15, 17, 86, 7]

for element in my_list:
    print('Начало цикла')
    func_with_params(param=element)
    print('Конец цикла')