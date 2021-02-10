# this is the welcome message to introduce a new exercise

class Message:
    pass

    @classmethod
    def welcome(cls, a):
        m = "This is an exercise to practise {0}.".format(a)
        return m

    @classmethod
    def check(cls, answer, result):
        # Error handling
        try:
            answer = float(answer)
        except ValueError:
            print("Please only use integer!")
        if answer == result:
            print("Answer is correct. Well Done!\n")
        else:
            print("Your answer is incorrect. The result is {0}\n".format(result))

    @classmethod
    def collect(cls, a):
        m = "Please enter the correct answer, {0}".format(a)
        return m
