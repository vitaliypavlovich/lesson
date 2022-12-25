'''
Получить сумму кубов натуральных чисел от n до m используя цикл for, числа n и m вводятся с клавиатуры.
'''
n = int(input('Введите n'))
m = int(input('Введите m'))
result = 0
for i in range(n, m + 1):
    result += i ** 3
print(result)
