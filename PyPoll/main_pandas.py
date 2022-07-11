#import modules
import os
import csv
import pandas as pd

#path for csv file
poll_csv = os.path.join("Resources", "election_data.csv")

Cand_Option = []
count = []
percent_cand = []
big = 0

poll_file_df = pd.read_csv(poll_csv)
poll_file_df.head()

#finds who got votes
Cand_Option = poll_file_df["Candidate"].unique()

#counts how many votes each candidate got
count = poll_file_df["Candidate"].value_counts()

#calculates the percent of votes each candidate got based off the total
percent_cand = (count/(len(poll_file_df)))*100
print(count)

print(Cand_Option)

print("-------------------------")
print("-------------------------")
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(len(poll_file_df)))
print("-------------------------")
for i in range(len(Cand_Option)):
   print(Cand_Option[i] + ": " + str(round(percent_cand[i],3)) + "%  " + "(" + str(count[i]) + ")")
print("-------------------------")
#prints winner of election

