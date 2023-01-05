'''
Пользователь вводит с клавиатуры числа до тех пор,
пока не введет любой строчный символ, из этих чисел составляется первый список.
Далее таким же образом вводятся второй и третий списки. Вывести на экран список, элементы которого есть в первых
двух списках, но отсутствуют в третьем.
'''

my_dict = {1: [], 2: [], 3: []}

for index, lst in my_dict.items():
    while True:
        n = input('Введите числа ')
        if n.isnumeric():
            lst.append(n)
        else:
            break
all_elements = set(my_dict[1] + my_dict[2])
result = []
for element in all_elements:
    if element not in my_dict[3]:
        result.append(element)
print(result)
