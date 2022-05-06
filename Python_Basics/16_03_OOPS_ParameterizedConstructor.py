# /**
# * @author Rajat Verma
# * https://www.linkedin.com/in/rajat-v-3b0685128/
# * https://github.com/rajatt95
# * https://rajatt95.github.io/
# *
# * Course: Learn API Automation Testing with Python & BDD Framework (https://www.udemy.com/course/python-sdet-rest-api-automation/)
# * Tutor: Rahul Shetty (https://www.udemy.com/user/rahul445/)
# */
#
# /***************************************************/

# Class
class MyCalculator:
    # Class - START

    # Class variable
    num = 100 # Properties/Data Member

    # Default Constructor
    def __init__(self):
        print("I'm in Default Constructor")

    # Parameterized Constructor
    def __init__(self, num1, num2):
        print("I'm in Parameterized Constructor")
        # print(num1 + num2)
        self.number1 = num1 # number1 -> Instance variable
        self.number2 = num2 # number2 -> Instance variable
        print(self.number1 + self.number2)

# Class - END

# Create an object of class
myCalculator_Object = MyCalculator(10, 20) # I'm in Parameterized Constructor | 30

print('********')

myCalculator_Object2 = MyCalculator(40, 50) # I'm in Parameterized Constructor | 90
