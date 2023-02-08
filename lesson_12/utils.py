from sqlalchemy.orm import sessionmaker

from lesson_12.models import Base


def create_table(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()