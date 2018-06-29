import csv
import sys

with open('budget_data.csv') as csvfile:

    readCSV = csv.reader(csvfile, delimiter=',')
    header =next(readCSV)
    dates = []
    revs = []

    for row in readCSV: 
        date = row[0]
        rev = int(row[1]) 

        dates.append(date)
        revs.append(rev)

Months = int(len(dates))
ProfLoss = sum(revs)

yearly_change =[]
for i in range(1,len(revs)):
        change = revs[i] - revs[i-1]
        yearly_change.append(change)
total_change = int(sum(yearly_change))
AvgChang= int(total_change/Months)

# AvgChang = int(ProfLoss/Months)
Increase = int(max(revs))
Decrease = int(min(revs))
MaxMonth = revs.index(Increase)
MinMonth = revs.index(Decrease)

print(" ")
print("Financial Analysis")

print("-"*32)

print(f'Total Months:  {Months}')
print(f'Total Profit/Losses: $ {ProfLoss}' )
print(f'Average Change: $ {AvgChang}' )
print(f'Greatest Increase in Profits: {dates[MaxMonth]} $ {Increase}' )
print(f'Greatest Decrease in Profits: {dates[MinMonth]} $ {Decrease}' )

# sys.stdout = open('PyBank_Analysis.txt', 'w')

with open ("PyBank_Analysis.txt", 'w') as text_file:
        text_file.write(" ")
        text_file.write("Financial Analysis\n")
        text_file.write("----------------------------------------------\n")
        text_file.write(f'Total Months:  {Months}\n')
        text_file.write(f'Total Profit/Losses: $ {ProfLoss}\n' )
        text_file.write(f'Average Change: $ {AvgChang}\n' )
        text_file.write(f'Greatest Increase in Profits: {dates[MaxMonth]} $ {Increase}\n' )
        text_file.write(f'Greatest Decrease in Profits: {dates[MinMonth]} $ {Decrease}\n' ) 