import csv
import os
election_data = '/Users/Satinder Bains/Desktop/Data3/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv'
with open(election_data, 'r') as election_data:
    csvreader = csv.reader(election_data, delimiter=',')
    next(csvreader)
    tot_votes = []
    candidates = []
    unique_candidates = {}
    #Loop through the data
    for col in csvreader:
        tot_votes.append(col[0])
        candidates.append(col[2])
        if col[2] not in unique_candidates:
            unique_candidates[col[2]] = 1
        else:
            unique_candidates[col[2]] += 1
#Create variables to refer to dictionary values
khan_votes = unique_candidates["Khan"]
correy_votes = unique_candidates["Correy"]
li_votes = unique_candidates["Li"]
otooley_votes = unique_candidates["O'Tooley"]
#Create variables to hold total percentage of vote recieved
k_percent = int(khan_votes / len(tot_votes) *100)
c_percent = int(correy_votes / len(tot_votes) *100)
l_percent = int(li_votes / len(tot_votes) *100)
o_percent = int(otooley_votes / len(tot_votes) *100)
print('Election Results\n----------------')
print("Total Votes:", len(tot_votes))
print('---------------------')
print('Khan:', khan_votes, 'votes', k_percent,'%')
print('Correy:', correy_votes, 'votes', c_percent,'%' )
print('Li:', li_votes, 'votes', l_percent,'%')
print("O'Tooley:", otooley_votes, "votes",o_percent,'%')
print("----------\nWINNER: Khan")
