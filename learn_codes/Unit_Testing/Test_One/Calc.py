import operator as op
class Calculator:
    def add(self, a, b):
            return op.add(a, b)

    def subtract(self, a, b):
        return op.sub(a, b)

    def mul(self, a, b):
            return op.mul(a, b)

    def floor_div(self, a, b):
            if b is 0:
                raise ValueError("Cannot Divide By Zero")

            return a / b

    def div(self, a, b):
            if b is 0:
                raise ValueError("Cannot Divide By Zero")

            return a//b

    def power(self, a, b):
            return op.pow(a, b)