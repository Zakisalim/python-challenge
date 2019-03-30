import csv
import os
csvfile_path= os.path.join("PyPoll\","election_data.csv")
with open(csvfile_path, newline="") as csvfile:
    csvreder=csv.reader(csvfile, delimiter=",")
    headers=next(csvreder)
    voters= []
    canadidates=[]
    candiate_name=[]
    count_khan=0
    count_correy=0
    count_li=0
    for row in csvreder:
        voters.append(row[0])
        total_number= len(voters)
        canadidate_name=row[2]
        if candiate_name not in candiates:
            canadidates.append(candiate_name)
            candiate_votes[candiate_name]=0
            candiate_votes=candiate_votes+1
            percent= candiate_votes/total_number

print("  Election Results ")
print("-----------------------")
print("Total Votes: " + str(total_number))
for candiates in candiates_votes:
    print(candiate_name, percent+"%", "("+candiate_votes+")")

output_path = os.path.join("PyPoll/", "output", "new.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ')

output_path = os.path.join("PyPoll/", "new.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ')
    csvwriter.writerow([total_number])
    csvwriter.writerow([candiate_name],[percent], [candiate_votes])
