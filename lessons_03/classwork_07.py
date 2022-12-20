'''
Создать переменную содержащую сторону квадрата, создать новый список, в котором будут периметр квадрата,
площадь квадрата и диагональ квадрата.
'''

side_square = int(input())

list = [side_square * 4, side_square * side_square, 2 ** 0.5 * side_square]

print(list)