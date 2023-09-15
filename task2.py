# Task2
# Calculator
# I made a calculator by python object-oriented programming which is based on classes and objects

# import abstract method to make a abstract class
from abc import ABCMeta, abstractmethod


# classes for basic mathematical operation
class Operation(metaclass=ABCMeta):

    def input_operands(self):
        self.operand_1 = int(input('Enter your First operand:'))
        self.operand_2 = int(input('Enter your second operand:'))

    @abstractmethod
    def matematical_operation(self):
        pass


class Addition_operation(Operation):

    def matematical_operation(self):
        self.input_operands()
        print('\nRESULT:\nAddition:', self.operand_1 + self.operand_2)


class Subtraction_operation(Operation):

    def matematical_operation(self):
        self.input_operands()
        print('\nRESULT:\nSubtraction:', self.operand_1 - self.operand_2)


class Multiplication_operation(Operation):

    def matematical_operation(self):
        self.input_operands()
        print('\nRESULT:\nMultiplication:', self.operand_1 * self.operand_2)


class Division_operation(Operation):

    def matematical_operation(self):
        self.input_operands()
        print('\nRESULT:\nDivision:', self.operand_1 / self.operand_2)


# main interface
print('**** HELLO PYTHON CALCULATOR ****')
print()
print("Here's your basic operation:")
print('PRESS[1] FOR ADDITION \nPRESS[2] FOR SUBTRACTION \nPRESS[3] FOR MULTIPLICATION \nPRESS[4] FOR DIVISION\n')
choice = int(input('Which operation you want to perform:'))

if choice == 1:
    a1 = Addition_operation()
    a1.matematical_operation()

elif choice == 2:
    s1 = Subtraction_operation()
    s1.matematical_operation()

elif choice == 3:
    m1 = Multiplication_operation()
    m1.matematical_operation()

elif choice == 4:
    d1 = Division_operation()
    d1.matematical_operation()

else:
    print('Invalid Choice!!\nPLS choose a given numbers')
