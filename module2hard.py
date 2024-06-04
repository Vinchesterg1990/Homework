n = int(input('Число в первой вставке (от 3 до 20): '))
result = []
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(len(elements)):
    for j in range(i+1, len(elements)):
        if n % (elements[i] + elements[j]) == 0:
            result.append((elements[i], elements[j]))
print(*result)
