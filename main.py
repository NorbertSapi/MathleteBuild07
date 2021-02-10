# This is m@thlete Build07

import random
from Student import Student
import Module

# collect data for the Student Object
first_name = input("What is your first name? ")
second_name = input("What is your second name? ")
age = input("How old are you? ")
gender = input("What is your gender? ")
email = input("What is your email address? ")
year = input("Please enter which school year are you in? ")
practise = int(input("Please enter which mathematical year would you like to practise: "))

# instantiate the Student object
student1 = Student(first_name, second_name, age, gender, email, year, practise)

# call method to generate user name
user_name = Student.get_user_name(first_name, second_name)
# print student1 first name, and greet the user.
print("Hello {0}, let's start practising.".format(student1.first_name, user_name))

x = random.randint(1, 10)
y = random.randint(1, 10)
f = random.randint(10, 100)
decimal = random.uniform(1, 10)
negative1 = - (random.randint(1, 10))
negative2 = - (random.randint(1, 10))
decimal1 = round(random.uniform(1, 10), 2)
decimal2 = round(random.uniform(1, 10), 2)


def module_1():
    Module.arithmetic_operators(x, y)
    Module.number_sense(x)
    Module.number_sense(y)
    Module.round_10(x)
    Module.round_10(y)
    Module.number_theory(x, y)


def module_2():
    Module.round_decimal(decimal)
    Module.exponents(x)
    Module.geometrics_measurement(x, y)


def module_3():
    Module.integers()
    Module.arithmetic_operators(negative1, negative2)
    Module.arithmetic_operators(decimal1, decimal2)
    Module.miles(y)
    Module.km(x)
    Module.equation(x, y, f)


def module_4():
    Module.integer_value(negative1)
    Module.integer_value(x)
    Module.pythagoras(x, y)
    Module.cos(x)
    Module.sin(x)
    Module.tan(x)


def test():
    if student1.practise == 6:
        module_1()
    elif student1.practise == 7:
        module_1()
        module_2()
    elif student1.practise == 8:
        module_1()
        module_2()
        module_3()
    elif student1.practise == 9:
        module_1()
        module_2()
        module_3()
        module_4()
    else:
        print("You entered a different mathematical year.\nWe might offer relevant mathematical exercise for different "
              "age in the future version.\nThank you, Good bye!")


def get_menu(a):
    Student.practise = a
    menu = {}
    if student1.practise == 6:
        menu = {1: "ARITHMETIC OPERATORS I.", 2: "NUMBER SENSE", 3: "PLACE VALUES", 4: "NUMBER THEORY",
                21: "TEST", 22: "EXIT"}
    elif student1.practise == 7:
        menu = {1: "ARITHMETIC OPERATORS I.", 2: "NUMBER SENSE", 3: "PLACE VALUES", 4: "NUMBER THEORY",
                5: "Round number", 6: "EXPONENTS AND SQUARE ROOTS", 7: "GEOMETRIC MEASUREMENT",
                21: "TEST", 22: "EXIT"}
    elif student1.practise == 8:
        menu = {1: "ARITHMETIC OPERATORS I.", 2: "NUMBER SENSE", 3: "PLACE VALUES", 4: "NUMBER THEORY",
                5: "Round number", 6: "EXPONENTS AND SQUARE ROOTS", 7: "GEOMETRIC MEASUREMENT", 8: "INTEGER NUMBERS - "
                "ARITHMETIC OPERATORS II.", 9: "DECIMAL NUMBERS - ARITHMETIC OPERATORS III.", 10: "UNIT OF MEASUREMENT",
                11: "EQUATION", 21: "TEST", 22: "EXIT"}
    elif student1.practise == 9:
        menu = {1: "ARITHMETIC OPERATORS I.", 2: "NUMBER SENSE", 3: "PLACE VALUES", 4: "NUMBER THEORY",
                5: "Round number", 6: "EXPONENTS AND SQUARE ROOTS", 7: "GEOMETRIC MEASUREMENT", 8: "INTEGER NUMBERS - "
                "ARITHMETIC OPERATORS II.", 9: "DECIMAL NUMBERS - ARITHMETIC OPERATORS III.", 10: "UNIT OF MEASUREMENT",
                11: "EQUATION", 12: "ABSOLUTE AND OPPOSITE VALUE", 13: "PYTHAGORAS THEOREM", 14: "TRIGONOMETRIC"
                "MEASUREMENT", 21: "TEST", 22: "EXIT"}

    while True:
        options = menu.keys()
        for entry in options:
            print(entry, menu[entry])

        selection = input("Enter your selection: ")
        # Error Handling: try/except
        try:
            selection = int(selection)
        except ValueError:
            print("Please only use integer!")
            get_menu(student1.practise)
        if 21 > selection > 4 and student1.practise == 6:
            get_menu(student1.practise)
        elif 21 > selection > 7 and student1.practise == 7:
            get_menu(student1.practise)
        elif 21 > selection > 11 and student1.practise == 8:
            get_menu(student1.practise)
        elif selection == 1:
            Module.arithmetic_operators(x, y)
        elif selection == 2:
            Module.number_sense(x)
            Module.number_sense(y)
        elif selection == 3:
            Module.round_10(x)
            Module.round_10(y)
        elif selection == 4:
            Module.number_theory(x, y)
        elif selection == 5:
            Module.round_decimal(decimal)
        elif selection == 6:
            Module.exponents(x)
        elif selection == 7:
            Module.geometrics_measurement(x, y)
        elif selection == 8:
            Module.integers()
            Module.arithmetic_operators(negative1, negative2)
        elif selection == 9:
            Module.arithmetic_operators(decimal1, decimal2)
        elif selection == 10:
            Module.miles(x)
            Module.km(y)
        elif selection == 11:
            Module.equation(x, y, f)
        elif selection == 12:
            Module.integer_value(x)
            Module.integer_value(negative1)
        elif selection == 13:
            Module.pythagoras(x, y)
        elif selection == 14:
            Module.cos(x)
            Module.sin(y)
            Module.tan(x)
        elif selection == 21:
            if student1.practise == 6:
                test()
            elif student1.practise == 7:
                test()
            elif student1.practise == 8:
                test()
            else:
                test()
        elif selection == 22:
            print("Thanks for practicing with m@thlete. See you soon!")
            break
        else:
            print("Please enter a  number from the menu!")


get_menu(student1.practise)
