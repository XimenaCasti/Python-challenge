import os
import csv

# Set path for file
csvpath = os.path.join(r"C:\Users\ximen\budget_data.csv") 

# Open the CSV using the UTF-8 encoding
with open(csvpath, newline='', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    print("Financial Analysis")
    print("______________________")

    # Skip the header row
    next(csvreader, None)

    # Initializing the variables 
    num_months = 0 # Starting in 0 to keep track of the amount of months 
    total_profit_losses = 0 #To get the amount 
    previous_profit_loss = 0 #Variable to store the average of previous month 
    changes = [] #List to store the monthly changes 
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 0
    greatest_decrease_month = ""

    # Loop through the data get the number of months 
    for row in csvreader:
        num_months += 1 #to get the number of months
        profit_loss = int(row[1]) # Casting to integer 
        total_profit_losses += profit_loss
    
        # Loop to calculate the change in profit or loss between the current month and the previous month and add this change to the changes list.    
        # Subtract the profit/loss value of the previous month (stored in previous_profit_loss) from the profit/loss value of the current month (stored in profit_loss) and store it in the change variable.
        if num_months > 1:
            change = profit_loss - previous_profit_loss
            #Store the result in the changes list storing the monthly changes  
            changes.append(change)
            if change > greatest_increase:
                #If the current change is the greatest increase til now, update the greatest_increase variable with the new biggest increase
                # and update the greatest_increase_month variable **0INDEX 
                greatest_increase = change
                greatest_increase_month = row[0]
                
            if change < greatest_decrease:
                ##If the current change is less than the greates_decrease til now, update the greatest_decrease variable with the new biggest decrease
                # and update the greatest_decrease_month variable **0INDEX 
                greatest_decrease = change
                greatest_decrease_month = row[0]
        previous_profit_loss = profit_loss
            
    print("Total months:", num_months)
    print("Total Profit/Losses:", total_profit_losses)

    # Calculate and print the average change
    average_change = sum(changes) / len(changes)
    print(f'Average Change: {average_change:.2f}')
    # Print the greatest increase in profits and the  month
    print("Greatest Increase in Profits:", greatest_increase_month, "($", greatest_increase, ")")

    # Print the greatest decrease in profits and the  month
    print("Greatest Decrease in Profits:", greatest_decrease_month, "($", greatest_decrease, ")")

    
