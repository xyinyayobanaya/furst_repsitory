def string_to_int(s):
    try:
        return int(s)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except (FileNotFoundError, IOError) as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Деление на ноль: {e}")
    except TypeError as e:
        print(f"Неправильный тип данных: {e}")
        return None

def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError as e:
        print(f"Индекс вне диапазона: {e}")
    except TypeError as e:
        print(f"Неправильный тип данных: {e}")
        return None