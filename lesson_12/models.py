from sqlalchemy import Integer, String, Column, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    profile = relationship("Profile", back_populates="user", uselist=False)
    addresses = relationship("Address", back_populates="user")
    purchases = relationship("Purchase", back_populates="user")

    def __str__(self):
        return f'User #{self.id}'

class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True)
    phone = Column(String)
    age = Column(Integer)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="profile", uselist=False)

    def __str__(self):
        return f'Profile #{self.user.email, self.age}'


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    city = Column(String)
    address = Column(String)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="addresses", uselist=False)

    def __str__(self):
        return f'Address #{self.city, self.address}'

class Purchase(Base):
    __tablename__ = "purchase"
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"))
    product_id = Column(ForeignKey("product.id"))
    count = Column(Integer)

    user = relationship("User", back_populates="purchases", uselist=False)
    product = relationship("Product", back_populates="purchases", uselist=False)

    def __str__(self):
        return f'Purchases #{self.user_id, self.product_id, self.count}'


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    count = Column(Integer)
    comment = Column(String)

    purchases = relationship("Purchase", back_populates="product")

    def __str__(self):
        return f'Product {self.id}, {self.name}, {self.price}, {self.count}, {self.comment}'

