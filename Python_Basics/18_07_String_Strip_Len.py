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

##### STRIP - START #####
stringWithSpaces = " RAJAT "
print(len(stringWithSpaces)) # 7

# strip() -> Removes the spaces from start and end
stringWithoutSpaces = stringWithSpaces.strip()
print(len(stringWithoutSpaces)) # 5

# lstrip() -> Removes the left space (Space from beginning)
stringWithoutLeftSpace = stringWithSpaces.lstrip()
print(len(stringWithoutLeftSpace)) # 6

# lstrip() -> Removes the right space (Space from ending)
stringWithoutRightSpace = stringWithSpaces.rstrip()
print(len(stringWithoutRightSpace)) # 6
##### STRIP - END #####