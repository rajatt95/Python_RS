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

# print(soup.prettify())
# table - Tag
# class is an Attribute and findList is the value
table_movies_thriller = soup.find('table', {'class': 'findList'})
# print(table_movies_thriller.prettify())

table_movies_thriller_Rows = table_movies_thriller.findAll('tr')
# print(table_movies_thriller_Rows)  # [<tr class="findResult odd"> <td class="primary_photo"> <a href="/title/tt0072285/"><img src="https://m.media-amazon.com/images/M/MV5BNTEwZjY3MjQtMGQ2Yi00NThhLThlZTItYjM4MmIwODVjNzY5XkEyXkFqcGdeQXVyMjUyNDk2ODc@._V1_UX32_CR0,0,32,44_AL_.jpg"/></a> </td> <td class="result_text"> <a href="/title/tt0072285/">Thriller - en grym film</a> (1973) </td> </tr>, <tr class="findResult even"> <td class="primary_photo"> <a href="/title/tt0164295/"><img src="https://m.media-amazon.com/images/M/MV5BOTQ0NTE2OTctM2ZjOS00MjFmLTg3NTMtZmM3ZGVjODAwYWQ5XkEyXkFqcGdeQXVyMTE1MTYxMzk2._V1_UX32_CR0,0,32,44_AL_.jpg"/></a> </td> <td class="result_text"> <a href="/title/tt0164295/">Thriller</a> (1973) (TV Series) </td> </tr>, <tr class="findResult odd"> <td class="primary_photo"> <a href="/title/tt0088263/"><img src="https://m.media-amazon.com/images/M/MV5BODhhZjJlYTktZDQ2MS00Yzk4LWFlOTQtYTgyOGE1ZGE5YWEyL2ltYWdlXkEyXkFqcGdeQXVyMzA5MjgyMjI@._V1_UX32_CR0,0,32,44_AL_.jpg"/></a> </td> <td class="result_text"> <a href="/title/tt0088263/">Michael Jackson: Thriller</a> (1983) (Music Video) </td> </tr>]

for row in table_movies_thriller_Rows:
    dataInRow = row.findAll('td')
    # a -> anchor tag
    print(dataInRow[1].a.text)  # Thriller - en grym film
    # Thriller
    # Michael Jackson: Thriller


