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

# Open the CSV file in Write mode
# Default mode -> Read
# w - write
# a - append
with open('./files/loanApp_write.csv', 'a') as csv_File:
    # csv_Writer is an object (has permission to append)
    csv_Writer = csv.writer(csv_File, delimiter=',')

    csv_Writer.writerow(["Rakesh", "Rejected"])

# Open the CSV file and read the data
with open('./files/loanApp_write.csv') as csv_File:
    # csv_Reader is an object
    csv_Reader = csv.reader(csv_File, delimiter=',')

    customer_names = []
    customer_status = []

    for row in csv_Reader:
        customer_names.append(row[0])
        customer_status.append(row[1])

print(customer_names)  # ['Name', 'Shreya', 'Kritika', 'Tanya', 'Sanya', 'Preeti', 'Deepti']
print(customer_status)  # ['Status', 'approved', 'rejected', 'approved', 'rejected', 'approved', 'rejected']

