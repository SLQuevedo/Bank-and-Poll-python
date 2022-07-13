#import modules
import os
import csv

#path for csv file
budget_csv = os.path.join("Resources", "budget_data.csv")
results_text = os.path.join("analysis", "PyBank_Analysis.txt")

#set up variables
months = 0
total_rev = 0
prev_rev = 0
rev_change = 0
avg_rev_change = 0
#no set length because we are inputting an unknown amount values into this array
list_rev_change = []
#array of length 2 to store the month in which it occurs and the value
bigInc = ["", 0]
bigDec = ["", 0]

#opening csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skips the header, it wont count that row
    next(csvfile, None)

    for row in csvreader:
        #counts our months
        months += 1
        
        #adds up all of our revenue
        total_rev = total_rev + int(row[1])

        #subtract the previous revenue from the current one to get our change in profits/losses
        rev_change = int(row[1]) - prev_rev

        #update the previous revenue value
        prev_rev = int(row[1])

        #puts our revenue changes in a list 
        list_rev_change = list_rev_change + [rev_change]

        #finds the greatest increase in revenue
        if rev_change > bigInc[1]:
            bigInc[1]= rev_change
            bigInc[0] = row[0]
        #finds the greatest decrease in revenue
        if rev_change < bigDec[1]:
            bigDec[1]= rev_change
            bigDec[0] = row[0]

#the list_rev_change contains the initial value of our profits/losses so we subtract it from our sum
#we subtract 1 from the length because we took out list_rev_change[0] value
#this gives us the average
avg_rev_change = (sum(list_rev_change) - list_rev_change[0])/(len(list_rev_change)-1)

#prints results     
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total Revenue: $" + str(total_rev))
print("Average Revenue change: $" + str(round(avg_rev_change,2)))
print("Greatest Increase in Profits: " + str(bigInc[0]) + " ($" + str(bigInc[1]) + ")")
print("Greatest Decrease in Profits: " + str(bigDec[0]) + " ($" + str(bigDec[1]) + ")")

#writes results into txt file
with open(results_text, "w") as txt_file:
    txt_file.write("Total Months: " + str(months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: $" + str(total_rev))
    txt_file.write("\n")
    txt_file.write("Average Revenue change: $" + str(round(avg_rev_change,2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Profits: " + str(bigInc[0]) + " ($" + str(bigInc[1]) + ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Profits: " + str(bigDec[0]) + " ($" + str(bigDec[1]) + ")")
