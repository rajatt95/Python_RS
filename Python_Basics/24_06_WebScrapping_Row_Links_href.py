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
soup = BeautifulSoup(responseData.content, 'html.parser')
table_movies_thriller = soup.find('table', {'class': 'findList'})
table_movies_thriller_Rows = table_movies_thriller.findAll('tr')

for row in table_movies_thriller_Rows:
    dataInRow = row.findAll('td')
    # a -> anchor tag
    print(dataInRow[1].a.text)  # Thriller - en grym film

    # Get the value of attribute 'href' in 'anchor' tag
    print(dataInRow[1].a['href'])  # /title/tt0072285/


