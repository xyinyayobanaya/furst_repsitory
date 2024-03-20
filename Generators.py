def all_variants(s):
    n = len(s)
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            yield s[start:start + length]

a = all_variants("abc")
for i in a:
    print(i)