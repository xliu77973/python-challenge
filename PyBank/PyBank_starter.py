# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = "Resources/budget_data.csv"  # Input file path
file_to_output = "analysis/budget_analysis.txt"  # Output file path

# Define variables to track the financial data
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.DictReader(financial_data)

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        total_revenue += int(row["Profit/Losses"])

        # Track the net change
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]
      
        # Calculate the greatest increase in profits (month and amount)
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        # Calculate the greatest decrease in losses (month and amount)
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# Calculate the average net change across the months
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# Generate the output summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_revenue}\n"
    f"Average Change: ${revenue_avg:.2f}\n"
    f"Greatest Increase in Profit: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Losses: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
