import os
import csv
import numpy as np

election_data = os.path.join('Resources', 'PyPoll.csv')

total_votes=0
candidate_list=[]
candidate_percent=0
election_winner= ""
votes_per_candidate= {}
winning_count = 0


with open(election_data) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    csv_header= next(csv_file)
    print(f"Header: {csv_header}")
  
    for row in csv_reader:
        total_votes +=1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            votes_per_candidate[row[2]]=0
        votes_per_candidate[row[2]] +=1 
        # candidate_list
        # candidate_percent


# print(votes_per_candidate)
    for total in votes_per_candidate:
        votes = votes_per_candidate[total]
        if votes > winning_count:
            winning_count=votes
            election_winner=total



print(f"total votes: {total_votes}")
print(f"candidate list:  {candidate_list}" )
print(f"winner: {election_winner} ")
print(f"percent of votes Li won: {round(votes_per_candidate['Li']/(total_votes)*100, 2)}")
print(f"percent of votes Correy won: {round(votes_per_candidate['Correy']/(total_votes)*100, 2)}")
print(f"percent of votes OTooley won: {round(votes_per_candidate['OTooley']/(total_votes)*100, 2)}")
print(f"percent of votes won by Khan: {round(votes_per_candidate['Khan']/(total_votes)*100, 2)}")
print(f"votes won by Khan: {votes_per_candidate['Khan']}")
print(f"votes won by Correy: {votes_per_candidate['Correy']}")
print(f"votes won by Li: {votes_per_candidate['Li']}")
print(f"votes won by O'Tooley: {votes_per_candidate(str[OTooley])}")


file_to_output = "pypoll.py"
with open(file_to_output, "w") as txt_file:
    
    txt_file.write("homework part 2")