'''
Используя условие первой задачи из урока, проверить то же самое только для коней.
'''

first = [5, 5]
second = [3, 3]

if __name__ == '__main__':
    if abs(first[0] - second[0]) == 1 and abs(first[1] - second[1]) == 2:
        print('YES')
    elif abs(first[1] - second[1]) == 1 and abs(first[0] - second[0]) == 2:
        print('YES')
    else:
        print('NO')