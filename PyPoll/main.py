import csv
import os
import collections
csvfile_path= os.path.join("PyPoll","election_data.csv")
with open(csvfile_path, newline="") as csvfile:
    csvreder=csv.reader(csvfile, delimiter=",")
    headers=next(csvreder)
    voters= []
    canadidtes=[]
    candiate_name=[]
    candiate_votes=0
    count_khan=0
    count_correy=0
    count_li=0
    for row in csvreder:
        voters.append(row[0])
        total_number= len(voters)
        candiate_name=(row[2])


    print("  Election Results ")
    print("-----------------------")
    print("Total Votes: " + str(total_number))
    if candiate_name not in canadidtes:
        canadidtes.append(candiate_name)
        candiate_votes=len(candiate_name)
        percent= candiate_votes/total_number

        for candiates in canadidtes:
            print(str(candiate_name),":", int(percent) ,"%", "(", float(candiate_votes),")")

output_path = os.path.join("PyPoll", "new.csv")
with open(output_path, newline='',mode='r+') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ')
    csvwriter.writerow([total_number])
    csvwriter.writerow([candiate_name])
    csvwriter.writerow([percent])
    csvwriter.writerow([candiate_votes])
