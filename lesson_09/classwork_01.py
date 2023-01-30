'''
Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).
Переопределить магические методы сложения, вычитания, умножения на число.
'''
from __future__ import annotations

class MyTime:
    hours = None
    minutes = None
    seconds = None


    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds
        self.timestamp = seconds + minutes * 60 + hours * 60 * 60

    def __eq__(self, other):
        return self.timestamp == other.timestamp

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return self.timestamp >= other.timestamp

    def __le__(self, other):
        return self.timestamp <= other.timestamp

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def __gt__(self, other):
        return self.timestamp > other.timestamp

    def __add__(self, other) -> MyTime:
        timestamp = self.timestamp + other.timestamp
        hours = timestamp // (60 * 60)
        minutes = (timestamp % (60 * 60)) // 60
        seconds = timestamp % 60
        return MyTime(hours, minutes, seconds)
    def __mul__(self, other) -> MyTime:
        timestamp = self.timestamp * other.timestamp
        hours = timestamp // (60 * 60)
        minutes = (timestamp % (60 * 60)) // 60
        seconds = timestamp % 60
        return MyTime(hours, minutes, seconds)
    def __sub__(self, other) -> MyTime:
        timestamp = self.timestamp - other.timestamp
        hours = timestamp // (60 * 60)
        minutes = (timestamp % (60 * 60)) // 60
        seconds = timestamp % 60
        return MyTime(hours, minutes, seconds)

    def __repr__(self):
        return f"MyTime: {self.hours, self.minutes, self.seconds}"

    def __str__(self):
        return f"MyTime: {self.hours, self.minutes, self.seconds}"

if __name__ == '__main__':
    time1 = MyTime(12, 12, 12)
    time2 = MyTime(12, 12, 12)
    print(time1.__sub__())
