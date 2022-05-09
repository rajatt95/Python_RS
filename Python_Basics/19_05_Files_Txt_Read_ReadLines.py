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

# readlines()
# -> This method helps to read line from txt file
# -> All the lines are stored in a list
# -> At 0th index: 1st line
lines = txtFileData.readlines()

print(lines)
print("lines[0]: "+lines[0])
print("lines[1]: "+lines[1])

print("$$$$$$$$$$$$$$$$$$$$$$$")

for line in lines:
    print(line)

txtFileData.close()

