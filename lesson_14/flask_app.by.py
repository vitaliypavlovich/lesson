import logging

from sqlalchemy import create_engine

from lesson_12.utils import create_table
from lesson_12.models import User, Profile, Address, Purchase, Product
from lesson_12.services import get_users
from lesson_12.services import create_user
from flask import Flask, request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)



# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         logger.info('Обрабатываю POST запрос')
#         for key, value in request.form.to_dict().items():
#             logger.info(f'{key}: {value}')
#         return 'hello world'
#
#     logger.info('Обрабатываю GET запрос')
#     for key, value in request.args.to_dict().items():
#         logger.info(f'{key}: {value}')
#     return 'hello world'
#
# @app.route("/", methods=["GET", "POST"])
# def abc():
#     if request.methon == 'POST':
#         logger.info('Обрабатываю POST за')

@app.route("/", methods=["GET"])
def index():
   return get_users(app.session)

@app.route("/", methods=["POST"])
def post_user():
    if not request.form.get('email') or not request.form.get('password'):
        raise Exception
    user = create_user(app.session, request.form.get('email'), request.form.get('password'))
    return {'user_id': user.id}


if __name__ == "__main__":
    engine = create_engine("postgresql://aloa:aloa@localhost/aloa")
    app.session = create_table(engine)
    app.run()

