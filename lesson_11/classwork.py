import sqlite3
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           INSERT INTO user (firstname, lastname, email, password, age)
           VALUES (?, ?, ?, ?, ?);
           """,
           (firstname, lastname, email, password, age),
       )
       session.commit()

def select_user(firstname: str):
   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           SELECT *
           FROM user
           WHERE firstname = ?;
           """,
           (firstname,)
       )
       session.commit()
       return cursor.fetchall()

def select_user_age(age_min: int, age_max: int):
    with sqlite3.connect('my_database.sqlite3') as session:
        cursor = session.cursor()
        cursor.execute(
            '''
            SELECT *
            FROM user
            WHERE age >= ? AND age <= ?;
            ''',
            (age_min, age_max)
        )
        session.commit()
        return cursor.fetchall()

def select_user_name_age(name_or_age):
    with sqlite3.connect('my_database.sqlite3') as session:
        cursor = session.cursor()
        cursor.execute(
            '''
            SELECT *
            FROM user
            WHERE firstname = ? OR age = ?
            ''',
            (name_or_age, name_or_age)
        )
        session.commit()
        return cursor.fetchall()
if __name__ == '__main__':
    #create_user("Alexander", "Chaika", "manti.by@gmail.com", "TestPass", 36)

    #create_user("Sanya", "Bulkin", "bulkin@gmail.com", "123", 25)

    #create_user("Vitaliy", "Pavlovich", "vitalliypavlovich@gmail.com", "321", 19)

    #create_user("Nikita", "Zaicev", "zaicev@gmail.com", "789", 20)

    #create_user("Vanya", "Kalinovsky", "kalinovsky@gmail.com", "987", 15)

    logger.info(select_user('Sanya'))

    logger.info(select_user_age(15, 25))

    logger.info(select_user_name_age(input('Введите имя или возраст ')))