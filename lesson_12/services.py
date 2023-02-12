from lesson_12.models import User, Address, Profile, Product, Purchase


def create_user(session, email, password, city, address, phone, age):
    user = User(email=email, password=password)
    session.add(user)
    session.commit()

    location = Address(user_id=user.id, city=city, address=address)
    session.add(location)

    profile = Profile(user_id=user.id, phone=phone, age=age)
    session.add(profile)

    session.commit()
    return user

def add_address(session, user_id, city, address):
    location = Address(user_id=user_id, city=city, address=address)
    session.add(location)
    session.commit()
    return location

def update_address(session, user_id, city, address):
    location = session.query(Address).filter(Address.user_id == user_id).first()

    location.address = address
    location.city = city

    session.add(location)
    session.commit()
    return location

def find_user(session, age):
    result = session.query(Profile).filter(Profile.age == age).first()
    return result

def create_product(session, name, price, count, comment):
    product = Product(name=name, price=price, count=count, comment=comment)
    session.add(product)
    session.commit()
    return product

def find_product(session, name):
    result = session.query(Product).filter(Product.name == name).first()
    return result

def update_product(session, product_id, name, price, count, comment):
    product = session.query(Product).filter(Product.id == product_id).first()

    product.name = name
    product.price = price
    product.count = count
    product.comment = comment

    session.add(product)
    session.commit()
    return product

def delete_product(session, product_id):
    product = session.query(Product).filter(Product.id == product_id).first()
    session.delete(product)
    session.commit()

def buy_product(session, email, product, count):
    user_id = session.query(User.id).filter(User.email == email)
    product_id = session.query(Product.id).filter(Product.name == product)
    purchase = Purchase(user_id=user_id, product_id=product_id, count=count)
    session.add(purchase)
    session.commit()

def find_purchase(session, email):
        user_id = session.query(User.id).filter(User.email == email)
        result = session.query(Purchase).filter(Purchase.user_id == user_id).first()
        return result