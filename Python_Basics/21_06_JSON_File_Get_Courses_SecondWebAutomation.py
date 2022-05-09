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

    # Extract the second Web Automation Course
    second_WebAutomation_Course = dictionary_courses['courses']['webAutomation'][1]
    print(second_WebAutomation_Course) # {'courseTitle': 'Cypress', 'price': '40'}

     # Extract the details from second Web Automation Course
    print("second_WebAutomation_Course['courseTitle']: "+second_WebAutomation_Course['courseTitle']) # Cypress
    print("second_WebAutomation_Course['price']: "+second_WebAutomation_Course['price']) # 40
