def all_variants(text):
    n = len(text)
    for i in range(1, n + 1):
        for start in range(n - i + 1):
            yield text[start:start + i]


a = all_variants("abc")
for i in a:
    print(i)
