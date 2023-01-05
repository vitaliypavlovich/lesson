'''
Вывести в порядке возрастания все простые числа, расположенные между n и m (включая сами числа n и m),
а также количество x этих чисел.
'''
n = int(input('Введите n'))
m = int(input('Введите m'))
my_list = []
x = 0
for i in range(n, m + 1):
    counter = 0
    for j in range(n, i + 1):
        if i % j == 0:
            counter += 1    # подсчет количества делителей
    if counter == 2:
        x += 1
        my_list.append(i)
my_list.sort()
print(my_list)
print('Количество простых чисел равно:', x)