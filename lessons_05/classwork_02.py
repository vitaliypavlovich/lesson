'''
Создать функцию, которая принимает на вход
неопределенное количество аргументов и возвращает их сумму и максимальное из них.
'''

def sum_and_max(*args):
    my_sum = 0
    my_max = args[0]
    if len(args):
        for element in args:
            my_sum += element
            if element > my_max:
                my_max = element
    return my_sum, my_max
result = sum_and_max(1, 3, 5, -1, 10)
print(result)