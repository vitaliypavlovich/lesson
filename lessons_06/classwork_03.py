'''
Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт,
где на первом месте номинал карты номинал (6 - 10, J, D, K, A),
а на втором название масти (Hearts, Diamonds, Clubs, Spades).
'''
from random import choice

def random_card(*card_rating, card_suit):
    random_rating = choice(card_rating)   #рандомный номинал
    random_suit = choice(card_suit)       #рандомная масть
    return random_rating, random_suit
print(random_card(*['6', '7', '8', '9', '10', 'J', 'D', 'K', 'A'], card_suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']))