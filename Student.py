# this is student class
# create student class
import random


class Student:
    pass

    # make init method, add attributes
    def __init__(self, first_name, second_name, age, gender, email, year, practise):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.gender = gender
        self.email = email
        self.year = year
        self.practise = practise

    # create user name using first and second name
    # create get_user_name
    @classmethod
    def get_user_name(cls, first_name, second_name):
        full_name = (first_name + " " + second_name).lower().split()
        if len(full_name) > 1:
            first_letter = full_name[0][0]
            three_letters_surname = full_name[-1][:3].rjust(3, 'x')
            number = '{:03d}'.format(random.randrange(1, 999))
            username = '{}{}{}'.format(first_letter, three_letters_surname, number)
            print("Your user name is: " + username)
        else:  # error handling for invalid input
            print('Error. Please enter first name and surname')
            cls.get_user_name(first_name, second_name)

    @classmethod
    def get_practise(cls):
        pass

        a = int(input("\nm@thlete offers different range of mathematical exercise for year 6 to 9."
                      " \nPlease enter which mathematical year would you like to practice for: "))
        try:
            a = int(a)
        except ValueError:
            print("Please enter a number. ")
        if 5 < a < 10:
            return a
        else:
            print("You entered a different mathematical year.")
