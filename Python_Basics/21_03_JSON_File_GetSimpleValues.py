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

    print(type(dictionary_courses)) # <class 'dict'>

    print(dictionary_courses) # {'instructor': 'RahulShetty', 'url': 'rahulshettycademy.com', 'services': 'projectSupport', 'expertise': 'Automation', 'courses': {'webAutomation': [{'courseTitle': 'Selenium Webdriver Java', 'price': '50'}, {'courseTitle': 'Cypress', 'price': '40'}, {'courseTitle': 'Protractor', 'price': '40'}], 'api': [{'courseTitle': 'Rest Assured Automation using Java', 'price': '50'}, {'courseTitle': 'SoapUI Webservices testing', 'price': '40'}], 'mobile': [{'courseTitle': 'Appium-Mobile Automation using Java', 'price': '50'}]}, 'linkedIn': 'https://www.linkedin.com/in/rahul-shetty-trainer/'}

    print("dictionary_courses['instructor']: "+dictionary_courses['instructor']) # RahulShetty
    print("dictionary_courses['url']: "+dictionary_courses['url']) # rahulshettycademy.com
    print("dictionary_courses['services']: "+dictionary_courses['services']) # projectSupport
    print("dictionary_courses['expertise']: "+dictionary_courses['expertise']) # Automation
    print("dictionary_courses['linkedIn']: "+dictionary_courses['linkedIn']) # https://www.linkedin.com/in/rahul-shetty-trainer/






