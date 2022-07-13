#import modules
import os
import csv
import pandas as pd

#path for csv file
poll_csv = os.path.join("Resources", "election_data.csv")
results_pd_text = os.path.join("analysis", "pandas_pypoll_Analysis.txt")

#initialize our variables
Cand_Option = []
count = []
percent_cand = []
big = 0
winner = ""

#reads file w pandas
poll_file_df = pd.read_csv(poll_csv)
poll_file_df.head()

#finds who got votes
Cand_Option = poll_file_df["Candidate"].unique()

#counts how many votes each candidate got
count = poll_file_df["Candidate"].value_counts()

#calculates the percent of votes each candidate got based off the total
percent_cand = (count/(len(poll_file_df)))*100

#finds the winner of the election
for candidate in Cand_Option:
   if count[candidate] > big:
      big = count[candidate]
      winner = candidate

#prints results
print("-------------------------")
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(len(poll_file_df)))
print("-------------------------")
#prints candidate results
for candidate in Cand_Option:
   print(candidate + ": " + str(round(percent_cand[candidate],3)) + "%  " + "(" + str(count[candidate]) + ")")
print("-------------------------")
print("Winner: " + winner)

#writes results
with open(results_pd_text, "w") as txt_file:
    txt_file.write("Total Votes: " + str(len(poll_file_df)))
    txt_file.write("\n")
#writes candidate results
    for candidate in Cand_Option:
        txt_file.write(candidate + ": " + str(round(percent_cand[candidate],3)) + "%  " + "(" + str(count[candidate]) + ") \n")
    txt_file.write("\n")
    txt_file.write("Winner: " + winner)
