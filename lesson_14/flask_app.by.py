import logging

from lesson_12.models import User, Profile, Address, Purchase, Product
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from lesson_12 import utils

from flask import Flask, request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        logger.info('Обрабатываю POST запрос')
        for key, value in request.form.to_dict().items():
            logger.info(f'{key}: {value}')
        return 'hello world'

    logger.info('Обрабатываю GET запрос')
    for key, value in request.args.to_dict().items():
        logger.info(f'{key}: {value}')
    return 'hello world'

@app.route("/", methods=["GET", "POST"])
def abc():
    if request.methon == 'POST':
        logger.info('Обрабатываю POST за')


if __name__ == "__main__":
    app.run()
