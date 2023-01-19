#import os module
import os

#module for reading csv files
import csv

election_csv = os.path.join('resources', 'election_data.csv')

vote_count = 0
vote_results = {}

previous_candidate_name = ''

with open(election_csv) as electionfile:
    reader = csv.reader(electionfile)

    header = next(reader)

    for row in reader:

        # add one to each iteration in loop
        vote_count += 1

        ballot_id = row[0]

        # a complete list of candidates who received votes
        candidate_name = row[2]

        if candidate_name in vote_results:
            vote_results[candidate_name] += 1

        else:
            vote_results[candidate_name] = 1
    


#print section

print()
print("Election Results:\n")

print("-------------------------\n")

print(f"Total Votes: {vote_count}\n")
print("-------------------------\n")

greatest_votes = -1

for candidate, votes in vote_results.items():

    print(f'{candidate}: {round(votes/vote_count*100,3)}% ({votes})\n')

    if votes > greatest_votes:
        greatest_votes = votes
        greatest_vote_candidate = candidate

    
print("-------------------------\n")
print(f"Winner: {greatest_vote_candidate}\n")
print("-------------------------\n")
