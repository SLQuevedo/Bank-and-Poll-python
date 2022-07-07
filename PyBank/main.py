#import modules
import os
import csv

#path for csv file
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

#set up variables
months = 0

#opening csv file
with open('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)

    for rows in budget_csv:

        months += 1

print(months)

