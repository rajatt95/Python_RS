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
with open('./files/MockResponse_GetCourse.json','r') as jsonFileReader:
    # load() -> This method helps to parse JSON file and returns dictionary
    dictionary_courses = json.load(jsonFileReader)

    # Goal: Extract the price of the Web Automation Course which has name 'Selenium Webdriver Java'
    webAutomation_Courses = dictionary_courses['courses']['webAutomation']
    print(webAutomation_Courses)

    # Iterating over a list to check which course has the price 50
    for webAutomation_Course in webAutomation_Courses:
        if webAutomation_Course['courseTitle'] == 'Selenium Webdriver Java':
            print(webAutomation_Course['price']) # 50
            break





