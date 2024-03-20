def is_prime(func):
    def is_prime_check(result):
        if result < 2:
            return "Составное"
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                return "Составное"
        return "Простое"

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        status = is_prime_check(result)
        print(status)
        print(result)

    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)