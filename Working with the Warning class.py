import warnings

def division_calculation(dividend, divisor):
    if abs(divisor) < 0.01:
        warnings.warn("Предупреждение: делитель близок к нулю, возможно деление на ноль", UserWarning)

    return dividend / divisor

# Фильтр always (всегда выводить предупреждения)
warnings.simplefilter("always")
result_always = division_calculation(10, 0.001)
print("Результат с фильтром always:", result_always)

# Фильтр ignore (игнорировать предупреждения)
warnings.simplefilter("ignore")
result_ignore = division_calculation(20, 0.001)
print("Результат с фильтром ignore:", result_ignore)

# Фильтр error (вызвать исключение при появлении предупреждения)
warnings.simplefilter("error")
try:
    result_error = division_calculation(30, 0.001)
except UserWarning as e:
    print("Исключение при фильтре error:", e)