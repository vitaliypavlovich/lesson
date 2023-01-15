'''
Дан список стран и городов каждой страны, где ключи это названия стран,
а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну.
Оформить в виде программы, которая считывает название города и выводит на печать страну.
'''

country_city = {
    'Belarus': ['Minsk', 'Vitebsk'], 'Spain': ['Madrid', 'Katalonia', 'Barcelona'], 'Italia': ['Milan', 'Venecia']
}
def finder(city):
    for key, value in country_city.items():
        if city in value:
            return key
if __name__ == '__main__':
    print(finder(input('Введите город')))