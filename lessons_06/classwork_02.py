'''
Доработать первое задание так, чтобы словарь читался из текстового CSV файла,
где на каждой строке пары слов вида: apple,яблоко.
'''
import csv

with open('dict.csv', 'r') as file:
    reader = csv.reader(file)
    dict = {
        row[0]: row[1]
        for row in reader
    }

def eng_to_rus(word):
    return dict.get(word)

def rus_to_eng(word):
    for eng, rus in dict.items():
        if rus == word:
            return eng

print(eng_to_rus('apple'))
print(rus_to_eng('Машина'))