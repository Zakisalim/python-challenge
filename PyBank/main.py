import csv
import os
csvfile_path= os.path.join("PyBank/","budget_data.csv")
with open(csvfile_path, newline="") as csvfile:
    csvreder=csv.reader(csvfile, delimiter=",")
    headers=next(csvreder)
    total=0
    averag=0
    min_value=0
    max_value=0
    profit_loss=[]
    for row in csvreder:
        profit_loss.append(row[1])
        number_of_months= len(profit_loss)
        total+=int(row[1])
        averag = int(total/number_of_months)

print("Financial Analysis")
print("------------------------")
print(" Total Months: " + str(number_of_months))
print("Total: $" + str(total))
print("Averag Change: " + str(averag))
