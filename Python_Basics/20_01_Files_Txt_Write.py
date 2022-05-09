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
# txtFileData = open('./files/TestData.txt')
#
# # read() -> This method helps to read all data from txt file
# print(txtFileData.read())
#
# txtFileData.close()
##############################

# Goal:
# -> Read the file and store all the lines in list
# -> Reverse the list
# -> Write he reversed content back to the file

# r -> Read mode
# w -> Write mode
with open('./files/TestData_Write.txt','r') as reader:
    listOfLines_PresentInFile = reader.readlines()
    #reversed(listOfLines_PresentInFile)
    with open('./files/TestData_Write.txt','w') as writer:
        for line in reversed(listOfLines_PresentInFile):
            writer.write(line)







