'''
1. Создать таблицу продуктов.
Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.

2. Создать программу с пользовательским интерфейсом позволяющим выбирать определенную функцию
и вводить необходимые данные.
'''
import sqlite3
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_product(product: str, price: int, amount: int, comment: str):
   with sqlite3.connect("homework_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           INSERT INTO user (product, price, amount, comment)
           VALUES (?, ?, ?, ?);
           """,
           (product, price, amount, comment)
       )
       session.commit()

def product_read(product_id):
    with sqlite3.connect('homework_database.sqlite3') as session:
        cursor = session.cursor()
        cursor.execute(
            '''
            SELECT *
            FROM user
            WHERE id = ?;
            ''',
            (product_id)
        )
        session.commit()
        return cursor.fetchall()

def product_update(product_id: int):
    with sqlite3.connect('homework_database.sqlite3') as session:
        cursor = session.cursor()
        cursor.execute(
            '''
            UPDATE user
            SET product = 'телефон'
            WHERE id = ?;
            ''',
            (product_id)
        )
        session.commit()

def product_delete(product_id: int):
    with sqlite3.connect('homework_database.sqlite3') as session:
        cursor = session.cursor()
        cursor.execute(
            '''
            DELETE FROM user
            WHERE id = ?;
            ''',
            (product_id)
        )
        session.commit()
if __name__ == '__main__':
    answer = int(input(
        'Выберите необходимое действие: '
        '1. Создать продукт. '
        '2. Прочитать всю информацию о продукте. '
        '3. Обновить информацию о продукте. '
        '4. Удалить продукт. '
    ))
    if answer == 1:
        create_product(input('Введите название продукта ').lower(), int(input('Введите цену ')), int(input('Введите количество ')), input('Введите комментарий '))
    elif answer == 2:
        logger.info(product_read(input('Введите ID продукта ')))
    elif answer == 3:
        product_update(input('Введите  ID продукта '))
    else:
        product_delete(input('Введите ID продукта '))
