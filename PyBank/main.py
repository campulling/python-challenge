# import modules

import os
import csv
# storage lists
months = []
profits = []
# set path to csv
budget_csv = os.path.join("Resources", "budget_data.csv")

# read csv and skip header 
with open (budget_csv, 'r') as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(budget_reader)

    # set loop for csv
    for row in budget_reader:

        #add date
        months.append(row[0])

        # add profits
        profits.append(int(row[1]))

# get total months
total_months = len(months)

# get total profits
total_profits = sum(profits)

# get average profit
average_change = total_profits / total_months

# get greatest increase in profits
max_increase = max(profits)

# get greatest loss in profits
max_loss = min(profits)

# use index to find dates
gain_index = profits.index(max_increase)
month_max = months[gain_index]
loss_index = profits.index(max_loss)
month_min = months[loss_index]

# Print Results
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: {total_profits}')
print(f'Average Change: {average_change:.2f}')
print(f'Greatest Increase in Profits: {month_max} {max_increase}')
print(f'Greatest Decrease in Profits: {month_min} {max_loss}')


# out put to file
text_file =  os.path.join("Analysis", "Financial_Analysis.txt")

with open (text_file, "w", newline='') as datafile:
    print('Financial Analysis\n'
'----------------------------\n'
f'Total Months: {total_months}\n'
f'Total: {total_profits}\n'
f'Average Change: {average_change}\n'
f'Greatest Increase in Profits: {month_max} {max_increase}\n'
f'Greatest Decrease in Profits: {month_min} {max_loss}', file=datafile)

 



