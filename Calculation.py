class Calculation:

    def __init__(self, weight, length):
        self.weight = weight
        self.length = length


def bmiCalculator(weight, length):
    bmi = weight / (length/100) **2
    return bmi