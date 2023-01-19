

# import modules
import os
import csv

# set path to csv
election_csv = os.path.join("Resources", "election_data.csv")

# dictionary storage
vote_counter = {}

votes_per = {}

total_votes = 0

# read csv and skip header
with open(election_csv, "r") as csvfile:
    election_reader = csv.reader(csvfile, delimiter=",")
    next(election_reader)

    # loop through data
    for row in election_reader:
    
        # count total votes
        total_votes = total_votes + 1 
    
        # count votes for the candidates
        if row[2] in vote_counter:
            vote_counter[row[2]] = vote_counter[row[2]] + 1
    
        else:
            vote_counter[row[2]] = 1

# set the variable for the winner
winner_votes = 0

# loop through votes to get vote percentage and winner
for candidate in vote_counter:

    # set percentage of votes per candidate
    votes_per[candidate] = (vote_counter[candidate] / total_votes) * 100

    # find out the winner
    if vote_counter[candidate] > winner_votes:
        winner_votes = vote_counter[candidate]
        winner = candidate


# print out text in terminal
print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")

for candidate, votes in vote_counter.items():
        print(f'{candidate}: {votes_per[candidate]:.3f}% ({votes})')
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")

#print out text in text file
# out put to file
text_file =  os.path.join("Analysis", "Financial_Analysis.txt")

with open (text_file, "w", newline='') as datafile:
    datafile.write(f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------\n''')
    for candidate, votes in vote_counter.items():
        datafile.write(f'   {candidate}: {votes_per[candidate]:.3f}% ({votes})\n')
    datafile.write(f'''
-------------------------
Winner: {winner}
-------------------------\n''')

