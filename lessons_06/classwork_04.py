'''
Использую функцию из предыдущей задачи, написать программу игру Блэкджек,
т.е. реализовать цикл в котором на каждом ходу у игрока спрашивается,
достать ли следующую карту, в случае положительного ответа  - вытягивать случайную карту.
Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го.
'''
from random import choice

def black_jack(*card_rating, **card_suits):
    total = 0
    while True:       #бесконечное количество итераций
        question = input('Достать ли следующую карту?').lower()    #преобразование к нижнему регистру
        if question != 'yes':
            print('Your total =', total)
            break
        all_cards = [*card_rating, *card_suits]      #упаковка списка и ключей словаря в один список
        random_card = choice(all_cards)              #выбор рандомной карты
        #прибавления очков если выпала карточка-картинка
        if random_card == 'Q' or random_card == 'K' or random_card == 'J' or random_card == 'A':
            print('Card =', random_card)
            total += card_suits[random_card]          #доступ к элементу словаря по ключу
        else:
            print('Card =', random_card)
            total += random_card
        print('Your total =', total)
        if total > 21:
            break
        elif total == 21:
            print('You win!')
            break
black_jack(*[i for i in range(2, 10 + 1)], Q = 10, K = 10, J = 10, A = 11)