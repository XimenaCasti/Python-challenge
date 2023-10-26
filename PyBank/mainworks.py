import os
import csv

# Set path for file
#csvpath = os.path.join("\\Resources\budget_data.csv") 
csvpath = os.path.join("Resources", "budget_data.csv")
csvpath_output = "financial_analysis.txt"

# Initializing the variables 
total_months = 0
previous_profit_loss = 0
Profit_Loss_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999999]
total_Profit_Loss = 0

# Open the CSV using the UTF-8 encoding
with open(csvpath, newline='', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader, None)

    # Loop through the data to get the number of months 
    for row in csvreader:
        total_months = total_months + 1
        total_Profit_Loss = total_Profit_Loss + int(row[1]) # Casting to integer 

        # Loop to calculate the change in profit or loss between the current month and the previous month   
        revenue_change = int(row[1]) - previous_profit_loss
        previous_profit_loss = int(row[1]) # Casting to integer 
        Profit_Loss_change_list.append(revenue_change)

        # Calculate greatest increase ** 0 = Date
        if revenue_change > greatest_increase[1]:
            greatest_increase[0] = row[0]  # 
            greatest_increase[1] = revenue_change
        # Calculate greatest decrease 
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]  
            greatest_decrease[1] = revenue_change

    # Calculate average revenue change
    revenue_average_change = sum(Profit_Loss_change_list) / len(Profit_Loss_change_list)

    # Output summary for cvs
    
    output = (
        f"Financial Analysis\n"
        f"------------------\n"
        f"Total Months: {total_months}\n"
        f"Total Profit/Losses: ${total_Profit_Loss}\n"
        f"Average Change: ${revenue_average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )
    print(output)

    # Export the results to a text file
    with open(csvpath_output, "w") as txt_file:
        txt_file.write(output)
