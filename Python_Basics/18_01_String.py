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


valueInString = "Test Automation Engineer"

# Value at given index
print("valueInString[0]: "+valueInString[0]) # T
print("valueInString[1]: "+valueInString[1]) # e
print("valueInString[2]: "+valueInString[2]) # s
print("valueInString[3]: "+valueInString[3]) # t

print("valueInString[-1]: "+valueInString[-1]) # r
# print("valueInString[30]: "+valueInString[30]) # IndexError: string index out of range

# Sub String
# 0 to n-1
print("valueInString[0:5]: "+valueInString[0:5]) # Test

# Concatenation
value1 = "Rajat"
value2 = "Verma"
print(value1+" "+value2) # Rajat Verma

# Find expected String
print("Test" in valueInString) # True
print("Rajat" in valueInString) # False

# Split String - on the basis of space
split_Str = valueInString.split(" ")
print(split_Str) # ['Test', 'Automation', 'Engineer']
print("split_Str[0]: "+split_Str[0]) # split_Str[0]: Test
print("split_Str[1]: "+split_Str[1]) # split_Str[1]: Automation
print("split_Str[2]: "+split_Str[2]) # split_Str[2]: Engineer
# print("split_Str[3]: "+split_Str[3]) # IndexError: list index out of range

##### STRIP - START #####
stringWithSpaces = " RAJAT "
print(len(stringWithSpaces)) # 7

# strip() -> Removes the spaces from start and end
stringWithoutSpaces = stringWithSpaces.strip()
print(len(stringWithoutSpaces)) # 5

# lstrip() -> Removes the left space (Space from beginning)
stringWithoutLeftSpace = stringWithSpaces.lstrip()
print(len(stringWithoutLeftSpace)) # 6

# rstrip() -> Removes the right space (Space from ending)
stringWithoutRightSpace = stringWithSpaces.rstrip()
print(len(stringWithoutRightSpace)) # 6
##### STRIP - END #####
