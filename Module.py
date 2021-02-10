import math
import random
from Message import Message
from MathModule import MathModule


# 1. ARITHMETIC OPERATORS
# this is a method to call arithmetic operators
def arithmetic_operators(a, b):
    # welcome message
    message = " arithmetical operation (addition, subtraction, multiplication, division) "
    print(Message.welcome(message))

    # addition exercise
    input_message = " {0} + {1}= ".format(a, b)
    result_addition = MathModule.add(a, b)
    answer_addition = input(Message.collect(input_message))
    Message.check(answer_addition, result_addition)

    # subtraction exercise
    input_message = " {0} - {1}= ".format(a, b)
    result_subtraction = MathModule.subtract(a, b)
    answer_subtraction = input(Message.collect(input_message))
    Message.check(answer_subtraction, result_subtraction)

    # multiplication exercise
    input_message = " {0} * {1}= ".format(a, b)
    result_multiplication = MathModule.multiple(a, b)
    answer_multiplication = input(Message.collect(input_message))
    Message.check(answer_multiplication, result_multiplication)

    # division exercise
    input_message = " {0} / {1}= ".format(a, b)
    result_division = MathModule.divide(a, b)
    round(result_division, 2)
    answer_division = input(Message.collect(input_message))
    Message.check(answer_division, result_division)


# 2 - 3. PLACE VALUES AND NUMBER SENSE:
def number_sense(a):
    # welcome message
    message = " place values and number sense "
    print(Message.welcome(message))
    result_sense = MathModule.even_odd(a)
    answer_sense = input("Please enter '1' if {0} is even or '0' if it is odd number: ".format(a))
    Message.check(answer_sense, result_sense)


def round_10(a):
    # rounding to the nearest 10
    input_message = "the nearest 10 to {0}: ".format(a)
    result_round = round(a, -1)
    answer_round = input(Message.collect(input_message))
    Message.check(answer_round, result_round)


# 4. NUMBER THEORY
def number_theory(a, b):
    # welcome message
    message = " greatest common factor "
    print(Message.welcome(message))
    # greatest common factor
    input_message = "the GCF of {0} and {1}= ".format(a, b)
    result_gcf = math.gcd(a, b)
    answer_gcf = input(Message.collect(input_message))
    Message.check(answer_gcf, result_gcf)

    # least common multiple
    message = " least common multiple "
    print(Message.welcome(message))
    input_message = "the LCM of {0} and {1} = ".format(a, b)
    result_lcm = MathModule.lcm(a, b)
    answer_lcm = input(Message.collect(input_message))
    Message.check(answer_lcm, result_lcm)


# 5. DECIMALS
# round decimal numbers
def round_decimal(a):
    # welcome message
    message = " rounding decimal numbers to the nearest hundredth "
    print(Message.welcome(message))

    # create variables
    result_round = round(a, 2)
    answer_round = input("Please round {0} to the nearest hundredth: ".format(a))
    # call chek method
    Message.check(answer_round, result_round)


# 6. EXPONENTS AND SQUARE ROOT
def exponents(a):
    # welcome message
    message = " exponents and square root "
    print(Message.welcome(message))

    # create result variable
    power_of = random.randint(1, 4)
    a_result = math.pow(a, power_of)
    # input variable - collects answer from user
    input_message = " {0} power {1}:".format(a, power_of)
    a_answer = input(Message.collect(input_message))
    Message.check(a_answer, a_result)

    # square roots
    input_message = "the square root of {0}: ".format(a)
    result_sqrt = math.sqrt(a)
    answer_sqrt = input(Message.collect(input_message))
    Message.check(answer_sqrt, result_sqrt)


# 7. GEOMETRICS MEASUREMENT
# Area of Rectangle
def geometrics_measurement(a, b):
    # welcome message
    message = "geometrics measurement: area of rectangle and perimeter of triangle "
    print(Message.welcome(message))

    # create variables
    result_area = MathModule.multiple(a, b)
    answer_area = input("Please calculate the square_area of the given rectangle. One side of the rectangle "
                        "is {0} cm and the other side is {1} square centimeter.".format(a, b))
    # call check method
    Message.check(answer_area, result_area)

    # Perimeter of Triangle
    # create variable for third side
    c = random.randint(1, 10)
    result_perimeter = MathModule.add(a, b) + c
    answer_perimeter = input("Please calculate the perimeter of the given triangle if side a is {0} cm and side b "
                             "is {1} cm and side c is {2} cm long. Perimeter of the triangle is : ".format(a, b, c))
    Message.check(answer_perimeter, result_perimeter)


# 8. INTEGERS - ARITHMETIC OPERATORS 2.
def integers():
    # welcome message
    message = " arithmetical operations using positive and negative numbers "
    print(Message.welcome(message))


# 9. DECIMAL NUMBERS - ARITHMETIC OPERATORS 3.
def decimals():
    # message
    message = " arithmetical operations using decimal numbers "
    print(Message.welcome(message))


# 10. UNIT OF MEASUREMENT
def miles(a):
    # welcome message
    message = "unit of measurement "
    print(Message.welcome(message))

    # "km to miles (1 km is 0.6214 miles)
    # variable to count difference between km and miles
    km_to_miles = 0.6214

    result_km_to_miles = MathModule.multiple(a, km_to_miles)
    answer_km_to_miles = input("Convert {0} km to miles. Please enter your answer: ".format(a))
    Message.check(answer_km_to_miles, result_km_to_miles)


def km(a):
    # variable to calculate difference between miles and km
    # miles to km (1 mile is 1.6093 km)
    miles_to_km = 1.6093
    result_miles_to_km = MathModule.multiple(a, miles_to_km)
    answer_miles_to_km = input("Convert {0} miles to km. Please enter your answer: ".format(a))
    Message.check(answer_miles_to_km, result_miles_to_km)


# 11. ONE VARIABLE EQUATION
# create equation method
def equation(a, b, c):
    # welcome message
    message = " to solve the equation. "
    print(Message.welcome(message))

    input_message = "to solve {0} * x + {1} = {2} ".format(a, b, c)

    # create variables result and answer
    result_equation = MathModule.linear_equation(a, b, c)
    answer_equation = input(Message.collect(input_message))

    # call check method
    Message.check(answer_equation, result_equation)


# 12. ABSOLUTE AND OPPOSITE VALUE
def integer_value(a):
    # welcome message
    message = " absolute and opposite value of in integer number"
    print(Message.welcome(message))

    # create input message
    input_message1 = " absolute value of {0} = ".format(str(a))
    input_message2 = " opposite value of {0} = ".format(a)

    # create variables
    result_absolute = abs(float(a))
    result_opposite = - float(a)
    answer_absolute = input(Message.collect(input_message1))
    # call check method
    Message.check(answer_absolute, result_absolute)

    # create answer_opposite variable
    answer_opposite = input(Message.collect(input_message2))
    # call check method
    Message.check(answer_opposite, result_opposite)


# 13. PYTHAGORAS THEOREM
# Create pythagoras theorem method
def pythagoras(a, b):
    # welcome message
    message = " Pythagoras Theorem "
    print(Message.welcome(message))

    # chose module, which side of the triangle would you like to calculate
    print('Assume the sides are a, b, c and c is the hypotenuse (the side opposite the right angle')
    case = input('Which side (a, b, c) do you wish to calculate? side> ')
    #
    # create variable for side 'c'
    c = float(random.randint(1, 10))

    #
    # if statement to chose formula 'c' or 'a' or 'b'
    # case 'c'
    if case == 'c':
        answer_c_side = input("Side 'a' is {0} and side 'b' is {1} calculate side 'c'. Your answer is: "
                              .format(a, b))
        result_c_side = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
        Message.check(answer_c_side, result_c_side)
    # case 'a'
    elif case == 'a':
        answer_a_side = input("Side 'c' is {0} and side 'b' is {1} calculate side 'a'. Your answer is: "
                              .format(c, b))
        result_a_side = math.sqrt(math.pow(c, 2) - math.pow(b, 2))
        Message.check(answer_a_side, result_a_side)
    # case 'b'
    elif case == 'b':
        answer_b_side = input("Side 'c' is {0} and side 'a' is {1} calculate side 'b'. Your answer is: "
                              .format(c, a))
        result_b_side = math.sqrt(math.pow(c, 2) - math.pow(a, 2))
        Message.check(answer_b_side, result_b_side)
    else:
        print('Please select a side between a, b, c')


# 14. TRIGONOMETRIC
# Create Trigonometric Functions
def cos(a):
    message = " trigonometric functions - cosine, sinus, tangent"
    print(Message.welcome(message))
    # calculate cosine
    # create variables cosine
    # input message to present exercise
    input_message = "cosine {0} = ".format(a)
    # calculate cosine
    result_cosine = math.cos(math.radians(a))
    # collect input answer
    answer_cosine = input(Message.collect(input_message))
    # call check method
    Message.check(answer_cosine, result_cosine)


def sin(a):
    # calculate sinus
    # input message to present exercise
    input_message = "sinus {0} = ".format(a)
    # calculate cosine
    result_sinus = math.sin(math.radians(a))
    # collect input answer
    answer_sinus = input(Message.collect(input_message))
    # call check method
    Message.check(answer_sinus, result_sinus)


def tan(a):
    # calculate tangent
    # input message to present exercise
    input_message = "tangent {0} = ".format(a)
    # calculate cosine
    result_tangent = math.tan(math.radians(a))
    # collect input answer
    answer_tangent = input(Message.collect(input_message))
    # call check method
    Message.check(answer_tangent, result_tangent)
