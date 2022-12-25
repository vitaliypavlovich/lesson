'''
Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран.
Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево
'''
# первый способ
text = input('Введите слово или фразу').lower() #преобразует строку в нижний регистр
text = ''.join(text.split()) #убирает все пробелы
if text == text[::-1]:
    print('yes')
else:
    print('no')

#второй способ
text = input().lower() #преобразует строку в нижний регистр
list_1 = []
list_2 = []
for i in text:
    if i == ' ':
        continue
    list_1.append(i)
for j in text[::-1]:
    if j == ' ':
        continue
    list_2.append(j)
if list_1 == list_2:
    print('yes')
else:
    print('no')

