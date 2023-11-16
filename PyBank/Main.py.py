import csv
import os

# Create Pathway to data
csv_Budget_Path = r"PyBank\Resources\budget_data.csv"
output_file_path = "budget_analysis.txt"
#create variables

total_sum = 0
total_months = 0
previous_change = 0
profit_loss_change = []
dates = []

with open(csv_Budget_Path, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    
    # Skip the header row
    header_row = next(csvreader, None)

    # Sum the values in the second column
    for row in csvreader:
        total_months += 1
        total_sum += float(row[1])
    
        # Calculate profit/loss change and add to the list
        current_profit_loss = float(row[1])
        if total_months > 1:
            change = current_profit_loss - previous_change
            profit_loss_change.append(change)
            dates.append(row[0])
        previous_change = current_profit_loss

# Find Average Change
average_change = sum(profit_loss_change) / len(profit_loss_change)

# Create nessesary definitions
def format_currency(value):
    return "${:,.2f}".format(value)

def find_max(profit_lose_change):
    mx = profit_loss_change[0]
    for num in profit_loss_change:
        if num > mx:
            mx = num
    return mx

def find_min(profit_lose_change):
    mn = profit_loss_change[0]
    for num in profit_loss_change:
        if num < mn:
            mn = num
    return mn

# Find Percent Changes for Min and Max

greatest_change_index = profit_loss_change.index(find_max(profit_loss_change))
lowest_change_index = profit_loss_change.index(find_min(profit_loss_change))

# Print to the Terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months:", total_months)
print("Total:", format_currency(total_sum))
print("Average Change:", format_currency(average_change))
print("Greatest Profit Increase:", dates[greatest_change_index], format_currency(find_max(profit_loss_change)))
print("Greatest Profit Decrease:", dates[lowest_change_index], format_currency(find_min(profit_loss_change)))
print("----------------------------")

# Export to a text file
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: {format_currency(total_sum)}\n")
    output_file.write(f"Average Change: {format_currency(average_change)}\n")
    output_file.write(f"Greatest Profit Increase: {dates[greatest_change_index]} {format_currency(find_max(profit_loss_change))}\n")
    output_file.write(f"Greatest Profit Decrease: {dates[lowest_change_index]} {format_currency(find_min(profit_loss_change))}\n")
    output_file.write("----------------------------\n")

print(f"Results have been exported to {output_file_path}")