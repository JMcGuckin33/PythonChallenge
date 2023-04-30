import os

import csv

with open("PyPoll/Resources/election_data.csv", "r") as f:
    csvreader = csv.reader(f, delimiter=',')
    #reading first row
    f_header = next(csvreader)
    #create variables
    voterids = []
    counties = []
    canidates = []
    canidate_names = []
    total_canidate_votes = []
    result_print = []
    canidate_percentage = []

    line_count=0
    winnercount=0
    losercount=0
    loop1=0
    loop2=0
    loop3=0
    loop4=0

    for row in csvreader:
        voterid=row[0]
        county=row[1]
        canidate=row[2]
        voterids.append(voterid)
        counties.append(county)
        canidates.append(canidate)

    line_count= len(voterids)

canidate_names.append(canidates[0])

for loop1 in range (line_count - 1):
    if canidates[loop1+1] != canidates[loop1] and canidates[loop1+1] not in canidate_names:
                 canidate_names.append(canidates[loop1+1])

n=len(canidate_names)

for loop2 in range(n):
      total_canidate_votes.append(canidates.count(canidate_names[loop2]))

print(canidate_names)
print(total_canidate_votes)


    
    






          
                  
