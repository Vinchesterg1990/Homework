def sum_three(a, b, c):
    return a + b + c


def is_prime(func):
    def wrapper(*args, **kwargs):
        sum_1 = func(*args, **kwargs)
        if sum_1 > 1:
            if all((sum_1 % i != 0) for i in range(2, int(sum_1 ** 0.5) + 1)):
                return 'Простое'
            else:
                return 'Составное'

    return wrapper

@is_prime
def sum_three(a, b, c):
    result = a + b + c
    print(result)
    return result

result = sum_three(2, 3, 6)
print(result)
