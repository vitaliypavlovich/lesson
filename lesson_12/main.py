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
from lesson_12.services import create_profile

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
    2. Создать профиль.
    3. Добавить новый адрес пользователя.
    4. Обновить адрес пользователя.
    5. Поиск всех пользователей с определенным возрастом.
    6. Создать продукт.
    7. Чтение продукта.
    8. Обновление продукта по ID.
    9. Удаление продукта по ID.
    10. Купить продукт.
    11. Показать все покупки пользователя.
    12. Фильтрация по произвольным параметрам.
    13. Выйти. '''

while True:
    logger.info(menu)
    print()
    choice = input('Выберите действие ')

    if choice == '1':
        email = input('Введите электронную почту ')
        password = input('Введите пароль ')

        user = create_user(session, email, password)

        logger.info(f'Пользователь #{user.id} создан')

    if choice == '2':
        email = input('Введите почту ')
        city = input('Введите город ')
        address = input('Введите адрес ')

        phone = input('Введите номер телефона ')
        age = input('Введите возраст ')

        profile = create_profile(session, email, city, address, phone, age)

        logger.info(f'Профиль Пользователя #{profile.user.id} создан')

    if choice == '3':
        email = input('Введите почту ')
        city = input('Введите город ')
        address = input('Введите адрес ')

        location = add_address(session, email, city, address)
        session.add(location)
        session.commit()

        logger.info(f'Пользователю 3{location.user.email} добавлен новый адрес')

    if choice == '4':
        email = input('Введите почту пользователя ')
        old_city = input('Введите старый город ')
        old_address = input('Введите старый адрес ')
        new_city = input('Введите новый город')
        new_address = input('Введите новый адрес')

        location = update_address(session, email, old_city, old_address, new_city, new_address)
        session.add(location)
        session.commit()
        logger.info(f'Адрес пользователя {location.user.email} обновлён')

    if choice == '5':
        age = input('Введите возраст пользователя ')
        result = find_user(session, age)
        logger.info(f'Найдены пользователи: {result}')

    if choice == '6':
        name = input('Введите название продукта ')
        price = input('Введите цену ')
        count = input('Введите количество ')
        comment = input('Введите комментарий ')

        product = create_product(session, name, price, count, comment)

        logger.info(f'Продукт {product.name} создан')
    if choice == '7':
        name = input('Введите название продукта ')

        product = find_product(session, name)
        logger.info(f'{product.name}, цена {product.price}, количество {product.count}, комментарий {product.comment}')
    if choice == '8':
        product_id = input('Введите ID продукта ')
        name = input('Введите название продукта ' )
        price = input('Введите цену ')
        count = input('Введите количество ')
        comment = input('Введите комментарий ')

        product = update_product(session, product_id, name, price, count, comment)
        logger.info(f'Продукт {product.name} обновлен')

    if choice == '9':
        product_id = input('Введите ID продукта ')
        product = delete_product(session, product_id)
        logger.info(f'Продукт #{product_id} удален ')

    if choice == '10':
        email = input('Введите email пользователя ')
        product = input('Введите название продукта ')
        count = input('Введите количество ')

        purchase = buy_product(session, email, product, count)
        logger.info(f'Покупка создана')

    if choice == '11':
        email = input('Введите email пользователя ')

        purchase = find_purchase(session, email)
        logger.info(f'{purchase.user.email}, {purchase.product.name}, количество {purchase.count}')
    # if choice == '12':
    #
    if choice == '13':
        exit()