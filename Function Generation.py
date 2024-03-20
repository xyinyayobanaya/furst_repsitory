def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x - y
        return subtract

my_func_add = create_operation("add")
print(my_func_add(1, 2))  # Выведет 3

# Лямбда-функция для умножения
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Выведет 6

# Аналог через def
def multiply_def(x, y):
    return x * y

print(multiply_def(2, 3))  # Выведет 6

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

rectangle = Rect(4, 5)
print(rectangle())  # Выведет 20
