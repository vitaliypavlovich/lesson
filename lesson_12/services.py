from lesson_12.models import User, Address, Profile, Product, Purchase


def create_user(session, email, password):
    user = User(email=email, password=password)
    session.add(user)
    session.commit()

    return user

def create_profile(session, email, city, address, phone, age):
    user_id = session.query(User.id).filter(User.email == email)
    location = Address(user_id=user_id, city=city, address=address)
    session.add(location)

    profile = Profile(user_id=user_id, phone=phone, age=age)
    session.add(profile)

    session.commit()
    return profile

def add_address(session, email, city, address):
    user_id = session.query(User.id).filter(User.email == email)
    location = Address(user_id=user_id, city=city, address=address)
    session.add(location)
    session.commit()
    return location

def update_address(session, email, old_city, old_address, new_city, new_address):
    user_id = session.query(User.id).filter(User.email == email)
    location = session.query(Address).filter(Address.user_id == user_id and Address.address == old_address
                                             and Address.city == old_city).first()

    location.address = new_address
    location.city = new_city

    session.add(location)
    session.commit()
    return location

def find_user(session, age):
    result = session.query(Profile.user_id).filter(Profile.age == age).all()
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

def get_users(session):
    users = session.query(User).all()
    return [u.as_dict() for u in users]