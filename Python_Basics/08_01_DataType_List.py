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

# In Python, a list is created by placing elements inside square brackets [] , separated by commas.
# A list can have any number of items and they may be of different types (integer, float, string, etc.).
# A list can also have another list as an item. This is called a nested list.

# The list is mutable.
valuesInList = [1, 1.1, "Python", 56, "Testing"]

print(valuesInList[0]) # 1
print(valuesInList[1]) # 1.1
print(valuesInList[2]) # Python
print(valuesInList[3]) # 56
print(valuesInList[4]) # Testing
# print(valuesInList[5]) #IndexError: list index out of range

# To get the last index of the list
print(valuesInList[-1]) # Testing

# To get the range for values at index of the list
print((valuesInList[1:4])) # [1.1, 'Python', 56]

# insert() -> Add an value at some index
valuesInList.insert(3, "Automation Testing") # Automation Testing will be added at the 3rd index of list
print(valuesInList) # [1, 1.1, 'Python', 'Automation Testing', 56, 'Testing']

# append() -> This will add the value at last index of list
valuesInList.append("END")
print(valuesInList) # [1, 1.1, 'Python', 'Automation Testing', 56, 'Testing', 'END']

# del -> Delete the value at given index
del valuesInList[0]
print(valuesInList) # [1.1, 'Python', 'Automation Testing', 56, 'Testing', 'END']



