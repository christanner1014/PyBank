import os
import csv

#Path
budget_data = os.path.join("Resources/budget_data.csv")

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#Read CVS
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)

    #Reading the first row 
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    #Rows of data
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])
        
        #Change and Add
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        total_pl = total_pl + int(row[1])

    #Biggest increase in profits
    biggest_inc = max(profits)
    biggest_profit = profits.index(biggest_inc)
    greatest_date = dates[biggest_profit]

    #Biggest Decrease
    biggest_dec = min(profits)
    biggest_loss = profits.index(biggest_dec)
    worst_date = dates[biggest_loss]

    #Find avg
    average_change = sum(profits)/len(profits)
    

#Print out info
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(average_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(biggest_inc)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(biggest_dec)})")

#Export
with open("Analysis.txt", "w") as output:
    output.write("Financial Analysis\n")
    output.write("---------------------\n")
    output.write(f"Total Months: {total_months}\n")
    output.write(f"Total: ${total_pl}\n")
    output.write(f"Average Change: ${round(average_change, 2)}\n")
    output.write(f"Greatest Increase in Profits: {greatest_date} (${biggest_inc})\n")
    output.write(f"Greatest Decrease in Profits: {worst_date} (${biggest_dec})\n")
