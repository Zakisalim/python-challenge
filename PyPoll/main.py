import csv
import os
import collections
csvfile_path= os.path.join("PyPoll/","election_data.csv")
with open(csvfile_path, newline="") as csvfile:
    csvreder=csv.reader(csvfile, delimiter=",")
    headers=next(csvreder)
    voters= []
    canadidates=[]
    count_khan=0
    count_correy=0
    count_li=0
    for row in csvreder:
        voters.append(row[0])
        total_number= len(voters)
        canadidates.append(row[2])
        count_khan= canadidates.count("khan")
        count_correy=canadidates.count("correy")
        count_li=canadidates.count("li")
        #if row[2]=="khan":
        #    count_khan=count_khan+1
        #elif row[2]=="correy":
            #count_correy=count_correy+1
        ##elif row[2]=="li":
            #count_li=count_li+1


print("  Election Results ")
print("-----------------------")
print("Total Votes: " + str(total_number))
print(count_khan)
print(count_correy)
print(count_li)
