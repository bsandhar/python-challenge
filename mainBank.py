import os
import csv

csv_path = '/Users/Satinder Bains/Desktop/Data3/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv'

with open(csv_path, newline="") as data:
    csvreader = csv.reader(data, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    monthavg = []
    profits = []
    months = []
    avgchange = []


    for col in csvreader:

        months.append((col[0]))
        profits.append(int(col[1]))


    print("Total Months:", len(months))
    print("Total Profits:", sum(profits))

    # i: 3
    for i in range(2,len(profits)):
        monthavg.append(profits[i] - profits[i-1])
        avgchange = sum(monthavg)/len(profits)

        max_profit = max(profits)
        min_profit = min(profits)



    print("Average Profits per Month: $", avgchange)
    print("Best Profit: $", max_profit)
    print("Worst Profit: $", min_profit)

# print(f"Total months: {months}")
# print(f"Total profit: {profits}")
# print(f"Average Profit: {monthavg}")
