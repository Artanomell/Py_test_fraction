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
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

    def __add__(self, other):
        common_denominator = fraction._lcm(self, self.denominator, other.denominator)
        num1 = int(self.numerator * common_denominator / self.denominator)
        num2 = int(other.numerator * common_denominator / other.denominator)
        return fraction(num1 + num2, common_denominator)

    def _lcm(self, a, b):
        m = a * b
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return m // (a + b)


inst1 = fraction(1, 2)
inst2 = fraction(2, 3)
inst3 = inst1 + inst2
print(inst3)

