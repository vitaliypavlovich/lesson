'''
Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow
'''

from lesson_08.library.dog import Dog
from lesson_08.library.cat import Cat

if __name__ == '__main__':
    dog = Dog(100, 50, 'My Dog', 10)

    dog.jump()
    dog.change_name('Dog')
    dog.run()
    dog.bark()

    cat = Cat(100, 50, 'My Cat', 10)

    cat.jump()
    cat.change_name('Wool')
    cat.run()
    cat.meow()