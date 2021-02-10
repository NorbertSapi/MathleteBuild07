import math


class MathModule:
    pass

    @classmethod
    def add(cls, x, y):
        # Add Function
        return x + y

    @classmethod
    def subtract(cls, x, y):
        # Subtraction Function
        return x - y

    @classmethod
    def multiple(cls, x, y):
        # Multiple Function
        return x * y

    @classmethod
    def divide(cls, x, y):
        # Divide function
        if y == 0:
            raise ValueError("Can not divide by zero!")
        return round((x / y), 2)

    @staticmethod
    def even_odd(a):
        if a % 2 == 0:
            x = 1
            return x
        else:
            x = 0
            return x

    @classmethod
    def lcm(cls, x, y):
        return abs(x * y) // math.gcd(x, y)

    @classmethod
    def linear_equation(cls, a, b, c):
        x = (c-b)/a
        return x
