'''
Пользователь вводит два числа N и M, рассчитать последовательность  N + NN + NNN + ... + NxM.
'''
from time import sleep
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# способ 2 + 22 + 222 ...
def my_func(N, M):
    result = N
    for term in range(2, M + 1):
        result = int(result) + int(N * term)    # 24 = 2 + int('2' * 2)
        sleep(1)
        yield result

if __name__ == '__main__':
    for element in my_func(input('Введите N '), int(input('Введите M '))):
        logger.info(element)


# способ 2 + (2 * 2) + (2 * 2 * 2) ...
def my_func(N, M):
    result = N
    for degree in range(2, M + 1):
        result += N ** degree    # 6 = 2 + (2 ** 2)
        sleep(1)
        yield result

if __name__ == '__main__':
    for element in my_func(int(input('Введите N ')), int(input('Введите M '))):
        logger.info(element)
