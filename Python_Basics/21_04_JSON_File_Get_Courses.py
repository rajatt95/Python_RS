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

# Open the JSON file and read the data
# r -> Read mode
# w -> Write mode
with open('./files/MockResponse_GetCourse.json', 'r') as jsonFileReader:
    # load() -> This method helps to parse JSON file and returns dictionary
    dictionary_courses = json.load(jsonFileReader)

    # print("dictionary_courses['courses']: " + dictionary_courses['courses'])  # TypeError: can only concatenate str (not "dict") to str
    print(dictionary_courses['courses']) # {'webAutomation': [{'courseTitle': 'Selenium Webdriver Java', 'price': '50'}, {'courseTitle': 'Cypress', 'price': '40'}, {'courseTitle': 'Protractor', 'price': '40'}], 'api': [{'courseTitle': 'Rest Assured Automation using Java', 'price': '50'}, {'courseTitle': 'SoapUI Webservices testing', 'price': '40'}], 'mobile': [{'courseTitle': 'Appium-Mobile Automation using Java', 'price': '50'}]}

    print(dictionary_courses['courses']['webAutomation']) # [{'courseTitle': 'Selenium Webdriver Java', 'price': '50'}, {'courseTitle': 'Cypress', 'price': '40'}, {'courseTitle': 'Protractor', 'price': '40'}]
    print(dictionary_courses['courses']['api']) # [{'courseTitle': 'Rest Assured Automation using Java', 'price': '50'}, {'courseTitle': 'SoapUI Webservices testing', 'price': '40'}]
    print(dictionary_courses['courses']['mobile']) # [{'courseTitle': 'Appium-Mobile Automation using Java', 'price': '50'}]

