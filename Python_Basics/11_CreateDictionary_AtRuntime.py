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
valuesInDictionary= {}

# KEY -> firstName, VALUE -> Rajat
valuesInDictionary['firstName'] = "Rajat"
valuesInDictionary['lastName'] = "Verma"
valuesInDictionary['github_profile'] = "https://github.com/rajatt95"
valuesInDictionary['github_page'] = "https://rajatt95.github.io/"
valuesInDictionary['linkedin_profile'] = "https://www.linkedin.com/in/rajat-v-3b0685128/"

print(valuesInDictionary["firstName"]) # Rajat
print(valuesInDictionary["lastName"]) # Verma
print(valuesInDictionary["github_profile"]) # https://github.com/rajatt95
print(valuesInDictionary["github_page"]) # https://rajatt95.github.io/
print(valuesInDictionary["linkedin_profile"]) # https://www.linkedin.com/in/rajat-v-3b0685128/


