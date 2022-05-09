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

# open() -> This method helps to open any txt file
txtFileData = open('./files/TestData.txt')

# read(20) -> This method helps to read first 20 characters from txt file
print(txtFileData.read(20))

txtFileData.close()
