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

import requests
from bs4 import BeautifulSoup

responseData = requests.get("https://www.imdb.com/find?q=thriller&ref_=nv_sr_sm")

# BeautifulSoup -> It will have the information about DOM
soup = BeautifulSoup(responseData.content, 'html.parser')

print(soup.prettify())











