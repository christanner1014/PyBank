import os
import csv

#Path

PyPollcsv = os.path.join("Resources/election_data.csv")


count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Read CVS

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        count += 1
        candidatelist.append(row[2])
    for x in set(candidatelist):
        unique_candidate.append(x)
        y = candidatelist.count(x)
        vote_count.append(y)
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
#Print out results
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes:" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(f"{unique_candidate[i]}: {vote_percent[i]:.3f}% ({vote_count[i]})") #*Come back later and reformat for 3 places*
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

#Export




with open("Results.txt", "w") as output:
    output.write("Election Results\n")
    output.write("---------------------------------------\n")
    output.write(f"Total Vote: {count}\n")
    output.write("---------------------------------------\n")
    for i in range(len(unique_candidate)):
        output.write(f"{unique_candidate[i]}: {vote_percent[i]:.3f}% ({vote_count[i]})\n")
    output.write("---------------------------------------\n")
    output.write(f"The winner is: {winner}\n")
    output.write("---------------------------------------\n")