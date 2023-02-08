import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from lesson_12.utils import create_table

from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists


from lesson_12.services import create_user
from lesson_12.services import add_address
from lesson_12.services import update_address
from lesson_12.services import find_user
from lesson_12.services import create_product
from lesson_12.services import find_product
from lesson_12.services import update_product
from lesson_12.services import delete_product
from lesson_12.services import buy_product
from lesson_12.services import find_purchase

DB_USER = "aloa"
DB_PASSWORD = "aloa"
DB_NAME = "aloa"
DB_ECHO = True


if __name__ == "__main__":
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,
    )
    if not database_exists(engine.url):
        create_database(engine.url)

    session = create_table(engine)

menu ='''
    1. Создать пользователя.
    2. Добавить новый адрес пользователя.
    3. Обновить адрес пользователя.
    4. Поиск всех пользователей с определенным возрастом.
    5. Создать продукт.
    6. Чтение продукта.
    7. Обновление продукта по ID.
    8. Удаление продукта по ID.
    9. Купить продукт.
    10. Показать все покупки пользователя.
    11. Фильтрация по произвольным параметрам.
    12. Выйти. '''

while True:
    logger.info(menu)
    print()
    choice = input('Выберите действие ')

    if choice == '1':
        email = input('Введите электронную почту ')
        password = input('Введите пароль ')

        city = input('Введите город ')
        address = input('Введите адрес ')

        phone = input('Введите номер телефона ')
        age = input('Введите возраст ')

        user = create_user(session, email, password, city, address, phone, age)

        logger.info(f'Пользователь #{user.id} создан')

    if choice == '2':
        user_id = input('Введите ID пользователя ')
        city = input('Введите город ')
        address = input('Введите адрес ')

        location = add_address(session, user_id, city, address)
        session.add(location)
        session.commit()

        logger.info(f'Пользователю 3{location.user.email} добавлен новый адрес')

    if choice == '3':
        user_id = input('Введите ID пользователя ')
        city = input('Введите город ')
        address = input('Введите адрес ')

        location = update_address(session, user_id, city, address)
        session.add(location)
        session.commit()
        logger.info(f'Адрес пользователя {location.user.email} обновлён')

    if choice == '4':
        age = input('Введите возраст пользователя ')
        result = find_user(session, age)
        logger.info(f'Найдены пользователи: {result.user.email}')

    if choice == '5':
        name = input('Введите название продукта ')
        price = input('Введите цену ')
        count = input('Введите количество ')
        comment = input('Введите комментарий ')

        product = create_product(session, name, price, count, comment)

        logger.info(f'Продукт {product.name} создан')
    if choice == '6':
        name = input('Введите название продукта ')

        product = find_product(session, name)
        logger.info(f'{product.name}, цена {product.price}, количество {product.count}, комментарий {product.comment}')
    if choice == '7':
        product_id = input('Введите ID продукта ')
        name = input('Введите название продукта ' )
        price = input('Введите цену ')
        count = input('Введите количество ')
        comment = input('Введите комментарий ')

        product = update_product(session, product_id, name, price, count, comment)
        logger.info(f'Продукт {product.name} обновлен')

    if choice == '8':
        product_id = input('Введите ID продукта ')
        product = delete_product(session, product_id)
        logger.info(f'Продукт #{product_id} удален ')

    if choice == '9':
        email = input('Введите email пользователя ')
        product = input('Введите название продукта ')
        count = input('Введите количество ')

        purchase = buy_product(session, email, product, count)
        logger.info(f'Покупка создана')

    if choice == '10':
        email = input('Введите email пользователя ')

        purchase = find_purchase(session, email)
        logger.info(f'{purchase.user.email}, {purchase.product.name}, количество {purchase.count}')
    # if choice == '11':
    #
    if choice == '12':
        exit()