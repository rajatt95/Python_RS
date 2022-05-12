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

import csv

# Open the CSV file and read the data
with open('./files/loanApp.csv') as csv_File:
    # csv_Reader is an object
    csv_Reader = csv.reader(csv_File, delimiter=',')

    for row in csv_Reader:
        print(row)  # ['Name', 'Status']
# ['Shreya', 'approved']
# ['Kritika', 'rejected']
# ['Tanya', 'approved']
# ['Sanya', 'rejected']
# ['Preeti', 'approved']
# ['Deepti', 'rejected']

