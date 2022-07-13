import csv
import os

#path for csv file
poll_csv = os.path.join("Resources", "election_data.csv")
results_text = os.path.join("analysis", "pypoll_Analysis.txt")

#initialize our total vote count
votes = 0 
#list of each candidate
Cand_Option = []
#as dict because we want to link candidate name with their votes
Cand_Votes = {}


with open(poll_csv) as pollfile:
    reader = csv.DictReader(pollfile)

    for row in reader:
        
        #counts TOTAL votes
        votes += 1

        if row["Candidate"] not in Cand_Option: 
            
            #adds our candidate into our dictionary of candidates
            Cand_Option.append(row["Candidate"])

            #counts the first vote for our candidate
            Cand_Votes[row["Candidate"]] = 1
    
        else:

            #counts up the votes for a specific candidate 
            Cand_Votes[row["Candidate"]] += 1

#using the max function, find the candidate with the most votes from our dict
winner = max(Cand_Votes, key=Cand_Votes.get)

print("-------------------------")
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(votes))
print("-------------------------")
for candidate in Cand_Votes:
   print(candidate + ": " + str(round((Cand_Votes[candidate]/votes)*100,3)) + "%  " + "(" + str(Cand_Votes[candidate]) + ")")
print("-------------------------")
print("Winner: " + winner)

with open(results_text, "w") as txt_file:
    txt_file.write("Total Votes: " + str(votes))
    txt_file.write("\n")
    for candidate in Cand_Votes:
        txt_file.write(candidate + ": " + str(round((Cand_Votes[candidate]/votes)*100,3)) + "%  " + "(" + str(Cand_Votes[candidate]) + ") \n")
    txt_file.write("\n")
    txt_file.write("Winner: " + winner)



