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

# Python Dictionary is an unordered sequence of data of key-value pair form.
# It is similar to the hash table type.
# Dictionaries are written within curly braces in the form key: value.
# It is very useful to retrieve data in an optimized way among a large amount of data.


# valuesInList = [1, 1.1, "Python", 56, "Testing"]
# valuesInTuple = (1, 1.1, "Python", 56, "Testing")
valuesInDictionary = \
    {
        27: "Age", # Key is number and Value is String
        "Name": "Rajat Verma", # Key is String and Value is also String
        7: "Sunday" # Key is number and Value is String
    }

# This is not based on the indexing
# valuesInDictionary[KEY] -> This will give the value
print(valuesInDictionary[27]) # Age
print(valuesInDictionary["Name"]) # Rajat Verma
print(valuesInDictionary[7]) # Sunday


