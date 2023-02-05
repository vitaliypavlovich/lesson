import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from lesson_12.models import Base, User, Address, Profile, Product, Purchase

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

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


    def create_user():
        user = User(email=input('Введите электронную почту '), password=input('Введите пароль '))
        session.add(user)
        session.commit()

        address = Address(user_id=user.id, city=input('Введите город '), address=input('Введите адрес '))
        session.add(address)

        profile = Profile(user_id=user.id, phone=input('Введите номер телефона '), age=input('Введите возраст '))
        session.add(profile)

        session.commit()

    def update_address():
        session.query(User).filter(User.email == input('Введите почту ')).first()
        address = session.query(Address).filter(Address.address == input('Введите старый адрес ')).first()
        address.address = input('Введите новый адрес ')
        session.add(address)
        session.commit()

    def add_address():
        address = Address(user_id=input('Введите ID '), city=input('Введите город '), address=input('Введите адрес '))
        session.add(address)
        session.commit()

    def find_user():
        result = session.query(Profile).filter(Profile.age == int(input('Введите возраст пользователя ')))
        for user in result:
            logger.info(user)

    def create_product():
        product = Product(name=input('Введите название продукта '), price=float(input('Введите цену ')),
                          count=int(input('Введите количество ')), comment=input('Введите комментарий '))
        session.add(product)
        session.commit()

    def read_product():
        result = session.query(Product).filter(Product.name == input('Введите название продукта '))
        for product in result:
            logger.info(product)

    def update_product():
        product = session.query(Product).filter(Product.id == int(input('Введите ID '))).first()
        product.name = input('Введите название продукта ')
        product.price = float(input('Введите цену '))
        product.count = int(input('Введите количество '))
        product.comment = input('Введите комментарий ')
        session.add(product)
        session.commit()

    def delete_product():
        product = session.query(Product).filter(Product.id == int(input('Введите ID '))).first()
        session.delete(product)
        session.commit()

    def buy_product():
        #product_id = session.query(Product.id).filter(Product.name == input('Введите название продукта' ))
        #user_id = session.query(User.id).filter(User.email == input('Введите почту'))
        purchase = Purchase(user_id=4, product_id=4, count='1')
        session.add(purchase)
        session.commit()



    #create_user()
    #update_address()
    #add_address()
    #find_user()


    #create_product()
    #read_product()
    #update_product()
    #delete_product()

    buy_product()