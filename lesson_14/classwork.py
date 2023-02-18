from flask import Flask, request
import logging
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