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
    num = 100 # Properties/Data Member

    # Function/Method
    # def getData(): # self is mandatory when creating functions inside the class
    def getData(self):
        # getData() - START
        print('Inside getData()')
        # getData() - END


# Class - END

# Create an object of class
myCalculator_Object = MyCalculator()

# Call properties and methods present in class
myCalculator_Object.getData()  # Inside getData()
print(myCalculator_Object.num)  # 100
