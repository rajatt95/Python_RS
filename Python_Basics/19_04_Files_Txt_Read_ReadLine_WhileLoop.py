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

# readline() -> This method helps to read line from txt file
line = txtFileData.readline() # FirstLine -> # /**

while line != "":
    print(line)
    line = txtFileData.readline()

txtFileData.close()




