"""
Написать класс, который реализует сущность "дробь", и позволяет складывать два экземпляра класса и печатать
экземпляр класса в виде дроби.
Пример использования:

inst1 = fraction(1, 2) # 1/2
inst2 = fraction(2, 3) # 2/3

inst3 = inst1 + inst2

print inst3
# 7/6
"""


class fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ('Divide by zero')

        if denominator < 0:
            self.denominator = -1 * denominator
            self.numerator = -1 * numerator
        else:
            self.numerator = numerator
            self.denominator = denominator

    def __str__(self):
        return '{0}/{1}'.format(self.numerator, self.denominator)

    def __add__(self, other):
        if self.numerator == 0 and other.numerator != 0:
            return other
        elif other.numerator == 0 and self.numerator != 0:
            return self
        else:
            common_denominator = fraction.__lcm(self, self.denominator, other.denominator)
            num1 = int(self.numerator * common_denominator / self.denominator)
            num2 = int(other.numerator * common_denominator / other.denominator)
            return fraction(num1 + num2, common_denominator)

    def __lcm(self, a, b):
        """
        Приватный метод нахождения наименьшего общего кратного целых чисел a и b
        честно утянул с http://younglinux.info/python/task/lcm
        :param a:
        :param b:
        :return:
        """
        m = a * b
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return m // (a + b)

#================ main ======================

inst1 = fraction(1, 2)
inst2 = fraction(2, 3)
inst3 = inst1 + inst2
print(inst3)