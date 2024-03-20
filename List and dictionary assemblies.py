nums = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

filtered_odd_squares = filter(lambda x: x % 2 != 0, map(lambda x: x ** 2, nums))

result = list(filtered_odd_squares)

print(result)