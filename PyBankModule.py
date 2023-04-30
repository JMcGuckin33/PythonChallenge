import os

import csv
total_profit = 0
total_months = 0
previous_month_profit = 0
total_change = 0
max_profit = 0
min_profit = 0 
max_profit_month = ""
min_profit_month = ""
with open("PyBank/Resources/budget_data.csv", "r") as f:
    csvreader = csv.reader(f)
    next(csvreader)
    for row in csvreader:
        month = row[0]
        profit = int(row[1])
        total_profit = total_profit + profit
        total_months = total_months + 1
        if total_months > 1:
            change = profit - previous_month_profit
            total_change = total_change + change
            if change > max_profit:
                max_profit = change 
                max_profit_month = month 
            if change < min_profit:
                min_profit = change
                min_profit_month = month 
        previous_month_profit = profit


with open("PyBank/analysis/analysis.txt", "w")as f:
    f.write("Financial Analysis\n")
    print("Financial Analysis")
    f.write("----------------------------\n")
    print("----------------------------")
    f.write(f"Total Months: {total_months}\n")
    print(f"Total Months: {total_months}")
    f.write(f"Total: ${total_profit}\n")
    print(f"Total: ${total_profit}")     
    f.write(f"Average Change: ${round(total_change/(total_months-1),2)}\n")
    print(f"Average Change: ${round(total_change/(total_months-1),2)}")
    f.write(f"Greatest Increase in Profits: {max_profit_month} (${max_profit})\n")
    print(f"Greatest Increase in Profits: {max_profit_month} (${max_profit})")
    f.write(f"Greatest Increase in Profits: {min_profit_month} (${min_profit})\n")
    print(f"Greatest Increase in Profits: {min_profit_month} (${min_profit})")

#total number of months included in the dataset
#net total amount of Profit/Loss over the entire period
#Changes in Profit/Loss over the entire period, and the average of those changes
#Greatest increase in profits (date and amount) over the entire period
#Greatest decrease in profits (date and amount) over the entire period

