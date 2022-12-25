'''
Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.
'''
from random import randint


my_list = []
x = randint(1, 20)
for i in range(x):
    y = randint(1, 100)
    my_list.append(y)
result = 0
for j in my_list:
    if j > 10:
        result += j
print(result)