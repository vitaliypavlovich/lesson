import logging

from sqlalchemy import create_engine

from lesson_12.utils import create_table
from lesson_12.models import User, Profile, Address, Purchase, Product
from lesson_12.services import get_users
from lesson_12 import services
from flask import Flask, request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# @app.route("/", methods=["GET"])
# def user_get():
#    return get_users(app.session)

# @app.route("/", methods=["POST"])
# def user_create():
#     if not request.form.get('email') or not request.form.get('password'):
#         raise Exception
#     user = services.create_user(app.session, request.form.get('email'), request.form.get('password'))
#     return {'user_id': user.id}

# @app.route('/', methods=['POST'])
# def profile_create():
#     profile = services.create_profile(app.session, request.form.get('email'), request.form.get('city'),
#                                       request.form.get('address'), request.form.get('phone'), request.form.get('age'))
#     return {'profile_id': profile.id}

# @app.route('/', methods=['POST'])
# def address_add():
#     location = services.add_address(app.session, request.form.get('email'), request.form.get('city'),
#                                       request.form.get('address'))
#     return {'location_id': location.id}

# @app.route('/', methods=['POST'])
# def address_update():
#     location = services.update_address(app.session, request.form.get('email'), request.form.get('old_city'),
#              request.form.get('old_address'), request.form.get('new_city'), request.form.get('new_address'))
#     return {'location_id': location.id}

# @app.route("/", methods=["GET"])
# def user_find():
#    return services.find_user(app.session)

# @app.route("/", methods=["POST"])
# def product_create():
#     product = services.create_product(app.session, request.form.get('name'), request.form.get('price'),
#                                       request.form.get('count'), request.form.get('comment'))
#     return {'product_id': product.id}

# @app.route('/', methods=['POST'])
# def product_update():
#     product = services.update_product(app.session, request.form.get('product_id'), request.form.get('name'),
#              request.form.get('price'), request.form.get('count'), request.form.get('comment'))
#     return {'product_id': product.id}

# @app.route('/', methods=['POST'])
# def product_delete():
#     product = services.delete_product(app.session, request.form.get('product_id'))

@app.route("/", methods=["POST"])
def purchase_create():
    purchase = services.buy_product(app.session, request.form.get('email'), request.form.get('product'),
                                      request.form.get('count'))
    return {'purchase_id': purchase.id}

if __name__ == "__main__":
    engine = create_engine("postgresql://aloa:aloa@localhost/aloa")
    app.session = create_table(engine)
    app.run()

