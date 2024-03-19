# Определяем собственные исключения
class InvalidDataException(Exception):
    pass

class ProcessingException(Exception):
    pass

# Функция, генерирующая исключения
def process_data(data):
    if not isinstance(data, int):
        raise InvalidDataException("Неверный тип данных. Ожидался целочисленный тип.")

    if data < 0:
        raise ProcessingException("Отрицательные данные не могут быть обработаны.")

    return data * 2

# Функции, вызывающие process_data и обрабатывающие исключения
def perform_data_processing(data):
    try:
        result = process_data(data)
    except InvalidDataException as e:
        print(f"Ошибка: {e}")
    except ProcessingException as e:
        print(f"Ошибка: {e}")
    else:
        print(f"Результат обработки данных: {result}")

# Вызываем функции и обрабатываем исключения
try:
    perform_data_processing("abc")
    perform_data_processing(-5)
    perform_data_processing(10)
except Exception as e:
    print(f"Произошла ошибка: {e}")