'''
Создать функцию при помощи регулярных выражений для проверки, что строка является валидным телефонным номером в формате
+375 (29) 299-29-29.
'''

import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def check_string(string):
    return re.search(r'^\+\d{1,3}\s\(\d{2}\)\s\d{3}\-\d{2}\-\d{2}$', string)

if __name__ == '__main__':
    test_string = input('Enter a string: ')
    math  = re.search(r'^\+\d{1,3}\s\(\d{2}\)\s\d{3}\-\d{2}\-\d{2}$', test_string)

    if math:
        logger.info(f'Found {math.group()}')
    else:
        logger.info('Did not find')