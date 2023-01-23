'''
Создать тест в отдельном файле и проверить несколько телефонных номеров.
'''

from lesson_10.classwork_01 import check_string



if __name__ == '__main__':
    assert check_string('+375 (29) 299-00-00') is not None
    assert check_string('+333333333333') is None
