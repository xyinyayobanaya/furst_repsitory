swift = ('my_list')
print(swift)
swift = ['apple', 'melon', 'mango', 'banana', 'lemon', 'peach']
print(swift)
index = swift.index("apple")
print(index)
index = swift.index("peach")
print(index)
print(swift[3:])
print(swift)
swift[3] = 'avocado'
print(swift)


my_dick = {'лимон':'lemon','апельсин':'orange','манго':'mango'}
print(my_dick)
print('Введите ключ')
key = input()
print(my_dick[key])

print('Введите ключ, значение которого будет изменено')
key = input()
my_dick[key] = 'change' + my_dick[key]
print(my_dick)