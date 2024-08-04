
def is_prime (func):
    def wrapper (*args):
        sum_1 = func(*args)
        if sum_1 > 1:
            if all((sum_1 % i != 0) for i in range(2, int(sum_1 ** 0.5) + 1)):
                return 'Простое'
            else:
                return 'Составное'
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)