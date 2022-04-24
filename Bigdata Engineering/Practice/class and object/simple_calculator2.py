class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        print(self.num1 + self.num2)

    def substraction(self):
        print(self.num1 - self.num2)

    def multiplication(self):
        print(self.num1 * self.num2)

    def division(self):
        print(self.num1 / self.num2)

clc = Calculator(10,3)
clc.addition()
clc.substraction()
clc.multiplication()
clc.division() 