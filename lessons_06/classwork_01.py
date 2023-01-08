'''
Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык.
Написать две функции, одна переводит слово с английского на русский, где слово - это входной параметр,
вторая функция - с русского на английский.
'''

dict = {'apple': 'Яблоко', 'car': 'Машина'}
def eng_to_rus(word):
    return dict.get(word)

def rus_to_eng(word):
    for eng, rus in dict.items():
        if rus == word:
            return eng

print(eng_to_rus('apple'))
print(rus_to_eng('Машина'))
