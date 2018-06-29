import csv
import operator

with open('election_data.csv') as csvfile:

    readCSV = csv.reader(csvfile, delimiter=',')
    header =next(readCSV)
    Candidates =[]

    for row in readCSV: 
        Candidate = row[2] 

        Candidates.append(Candidate)

Total = int(len(Candidates))

KTotal = int(Candidates.count("Khan"))
KP = "{0:.3f}".format((KTotal/Total)*100)
CTotal =  int(Candidates.count("Correy"))
CP = "{0:.3f}".format((CTotal/Total)*100)
LTotal = int(Candidates.count("Li"))
LP = "{0:.3f}".format((LTotal/Total)*100)
OTotal = int(Candidates.count("O'Tooley"))
OP = "{0:.3f}".format((OTotal/Total)*100)

Totals = [
    {'Name': 'Khan', 'VoteCount': KTotal}, 
    {'Name': 'Correy', 'VoteCount': CTotal}, 
    {'Name': 'Li', 'VoteCount': LTotal}, 
    {'Name': "O'Tooley", 'VoteCount': OTotal}
]

Names = [n['Name'] for n in Totals]
VoterCounts = [v['VoteCount'] for v in Totals]

MaxVC = max(VoterCounts)
MaxVCI = VoterCounts.index(MaxVC)
Winner = Names[MaxVCI]

print(" ")
print("Election Results")
print("-"*32)
print(f'Total Votes: {Total}')
print("-"*32)
print(f'Khan: {KP}% ({KTotal})')
print(f'Correy: {CP}% ({CTotal})')
print(f'Li: {LP}% ({LTotal})')
print(f"O'Tooley: {OP}% ({OTotal})")
print("-"*32)
print(f'Winner: {Winner}')
print("-"*32)

with open ("PyPoll_Analysis.txt", 'w') as f:
    f.write(" ")
    f.write("Election Results\n")
    f.write("----------------------------------------------\n")
    f.write(f'Total Votes: {Total}\n')
    f.write("----------------------------------------------\n")
    f.write(f'Khan: {KP}% ({KTotal})\n')
    f.write(f'Correy: {CP}% ({CTotal})\n')
    f.write(f'Li: {LP}% ({LTotal})\n')
    f.write(f"O'Tooley: {OP}% ({OTotal})\n")   
    f.write("----------------------------------------------\n")
    f.write(f'Winner: {Winner}\n')
    f.write("----------------------------------------------\n")