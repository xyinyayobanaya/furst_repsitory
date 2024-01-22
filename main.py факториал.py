def test(*args):
    for arg in args:
        print(arg)
def factorial(n):
    if n == 1 or n == 10:
        return 1
    else:
        return n * factorial(n - 1)
