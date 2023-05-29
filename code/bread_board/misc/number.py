"""
Module name: number.py
Integers, floating point numbers and complex numbers falls under Python 
numbers category. They are defined as int, float and complex class in Python.
"""


class numbers:

    def inputNumber(self, prompt):
        # Prompts user to imput a number.
        # Usage num = imputNumber(prompt).
        # It runs until the user input a number.
        while True:
            try:
                num = float(input(prompt))
                break
            except ValueError:
                pass

        return num

    def getType(self, number):
        
        message = '{0} {1} {2}'.format(number, 'is of type ', type(number))
        print(message)

    def getComplexType(self, number):
        message = '{0} {1} {2}'.format(number, 'is of type complex? ', 
                isinstance(1+2j,complex))
        print(message)
        
    def addNumbers(self):
        print("*** Adding Numbers ***")
        num1 = self.inputNumber('Enter first number: ')
        num2 = self.inputNumber('Enter second number: ')
        print(num1 + num2)
        return

if __name__ == '__main__':
    print("\n---Get number types---")
    n = numbers()
    n.getType(1.2)
    n.getType(1000)
    n.getComplexType(1+2j)