from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from lesson_12.models import Base, User, Profile, Address

DB_PATH = Path(__file__).resolve().parent / "my_database.sqlite3"
DB_ECHO = True


if __name__ == "__main__":
    engine = create_engine(f"sqlite:////{DB_PATH}", echo=DB_ECHO)
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


    def create_user():
        user = User(email="test@test.com", password="password")
        session.add(user)

        profile = Profile(phone='123', age='22', user_id=user.id)
        session.add(profile)

        address = Address(city='Minsk', address='beletskogo', user_id=user.id)
        session.add(address)
        session.commit()

    create_user()