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

# Inheritance
# MyCalculator -> Class
# Present in Z_17_001_Inheritance_ParentClass.py file
from Z_17_001_Inheritance_ParentClass import MyCalculator

# ScientificCalculator -> Child class
# MyCalculator -> Parent class
class ScientificCalculator(MyCalculator):
    # Class - START
    numFromChildClass = 100

    def getCompleteData(self):
         # getCompleteData() _ START
         # add(), sub() -> Methods present in Parent class
         print(self.add()) # MyCalculator - add()
         print(self.sub()) # MyCalculator - sub()
         # numFromChildClass -> Variable present in Child class
         print(self.numFromChildClass) # 100
        # getCompleteData() - END
# Class - END

# Create an object of class: ScientificCalculator
scientificCalculator_Object = ScientificCalculator()

# Call properties and methods present in class
scientificCalculator_Object.getCompleteData()
print(scientificCalculator_Object.numFromChildClass)  # 100






