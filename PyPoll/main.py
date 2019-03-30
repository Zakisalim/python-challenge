import csv
import os
canadidates={}
csvfile_path= os.path.join("PyPoll/","election_data.csv")
with open(csvfile_path, newline="") as csvfile:
    csvreder=csv.reader(csvfile, delimiter=",")
    headers=next(csvreder)
    voters= []
    for row in csvreder:
        voters.append(row[0])
        total_number= len(voters)
        voter_id, county, candidate= row
        if candidate not in canadidates:
            canadidates[candidate]= list()
        canadidates[candidate].append((county, voter_id))
print("  Election Results ")
print("-----------------------")
print("Total Votes: " + str(total_number))
