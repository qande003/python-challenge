#import os module
import os

#module for reading csv files
import csv

budget_csv = os.path.join('resources', 'budget_data.csv')

#set variable to -1 so it can exclude count of header
monthcount = 0

total_profit_losses = 0
total_profit_loss_change = 0
previous_profit_loss = 0
greatest_increase_profit = float('-inf')
greatest_decrease_profit = float('inf')

# list1 = ['Jan-10', '1088983']

# print(list1[0])

with open(budget_csv) as budgetfile:
    reader = csv.reader(budgetfile)

    header = next(reader)

    for row in reader:
        # print(row)

        # add one to each iteration in loop (will sum all rows in column)
        monthcount += 1

        row_date = row[0]

        # sum each line in profit/loss
        profit_loss = float(row[1])
        total_profit_losses = total_profit_losses + profit_loss

        #current row in "Profit/Loss" column - previous
        change_profit_loss = profit_loss - previous_profit_loss 

        #greatest increase in profits

        
        # print(f'row: {monthcount+1}')
        # print(profit_loss)
        # print(previous_profit_loss)
        # print(change_profit_loss)
        
        
        if monthcount > 1:
            total_profit_loss_change = total_profit_loss_change + change_profit_loss
            
            #greatest increase in profit
            
            if change_profit_loss > greatest_increase_profit:
                greatest_increase_profit = change_profit_loss
                greatest_increase_profit_date = row_date

            if change_profit_loss < greatest_decrease_profit:
                greatest_decrease_profit = change_profit_loss
                greatest_decrease_profit_date = row_date
        
        # store previous profit loss for next iteration
        previous_profit_loss = profit_loss

    
average_change = total_profit_loss_change / (monthcount - 1)

# print(total_profit_loss_change)
    
# print(total_profit_losses)
       
print("Financial Analysis\n")

print("----------------------------\n")

print(f"Total Months: {monthcount}\n")

print(f"Total: ${total_profit_losses}\n")

print(f"Average Change: ${average_change}\n")

print(f"Greatest Increase in Profits: {greatest_increase_profit_date} (${greatest_increase_profit})\n")

print(f"Greatest Decrease in Profits: {greatest_decrease_profit_date} (${greatest_decrease_profit})\n")
