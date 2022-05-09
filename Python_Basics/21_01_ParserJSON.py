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

import json

# 2 keys
# 1st key has a string value
# 2nd key has a list of string values
json_courses = '{"name":"Rahul Shetty", "languages": ["Java" , "Python", "Javascript"]}'

# loads() -> This method helps to parse JSON string and returns dictionary
dictionary_courses = json.loads(json_courses)

print(type(dictionary_courses)) # <class 'dict'>

print(dictionary_courses) # {'name': 'Rahul Shetty', 'languages': ['Java', 'Python', 'Javascript']}

# Extract the values using key
print("dictionary_courses['name']: "+dictionary_courses['name']) # dictionary_courses['name']: Rahul Shetty

print(dictionary_courses['languages']) # ['Java', 'Python', 'Javascript']

listOfLanguages = dictionary_courses['languages']

print("listOfLanguages[0]: "+listOfLanguages[0]) # listOfLanguages[0]: Java
print("listOfLanguages[1]: "+listOfLanguages[1]) # listOfLanguages[1]: Python
print("listOfLanguages[2]: "+listOfLanguages[2]) # listOfLanguages[2]: Javascript

for language in listOfLanguages:
    print(language)





