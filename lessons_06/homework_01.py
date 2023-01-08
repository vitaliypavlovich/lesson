'''
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное, в идеале не использовать библиотечные функции.
'''

def text(message):
    message = message.split()
    max = len(message[0])
    max_len = []
    for i in message:
        if len(i) >= max:
            max_len.append(i)
            max = len(i)
    print(max_len[-1])

text('Доброе утро друзья друзья утро утро')

