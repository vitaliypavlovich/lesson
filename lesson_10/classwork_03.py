'''
Создать генератор и/или итератор простой геометрической прогрессии.
'''

from time import sleep
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def geometric_progress():
    b1 = 3
    q = 4
    for n in range(1, 10):
        b = b1 * q **(n - 1)
        sleep(1)
        yield b

if __name__ == '__main__':
    for item in geometric_progress():
        logger.info(item)
